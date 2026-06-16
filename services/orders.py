from datetime import datetime

from database import (
    fetch_one,
    fetch_all,
    execute
)

from services.tables import (
    reserve_table,
    open_table
)



# ======================
# ORDER QUERIES
# ======================

def get_all_orders():

    return fetch_all(
        """
        SELECT
            o.*,
            t.table_no
        FROM orders o
        INNER JOIN restaurant_tables t
            ON t.id = o.table_id
        ORDER BY o.id DESC
        """
    )


def get_order_by_id(order_id):

    return fetch_one(
        """
        SELECT
            o.*,
            t.table_no
        FROM orders o
        INNER JOIN restaurant_tables t
            ON t.id = o.table_id
        WHERE o.id = %s
        """,
        (order_id,)
    )


def get_active_order(table_id):

    return fetch_one(
        """
        SELECT *
        FROM orders
        WHERE table_id = %s
        AND status IN (
            'pending',
            'preparing',
            'ready'
        )
        ORDER BY id DESC
        LIMIT 1
        """,
        (table_id,)
    )



# ======================
# ORDER CREATION
# ======================

def generate_order_no():

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    return f"ORD-{timestamp}"


def create_order(table_id):

    order_no = generate_order_no()

    order_id = execute(
        """
        INSERT INTO orders (
            order_no,
            table_id
        )
        VALUES (
            %s,
            %s
        )
        """,
        (
            order_no,
            table_id
        )
    )

    reserve_table(table_id)

    return order_id



# ======================
# ORDER ITEMS
# ======================

def add_item(    order_id,    menu_item_id,    qty=1):

    menu_item = fetch_one(
        """
        SELECT *
        FROM menu_items
        WHERE id = %s
        """,
        (menu_item_id,)
    )

    if not menu_item:
        raise Exception(
            "Menu item not found"
        )

    unit_price = float(
        menu_item["price"]
    )

    total_price = unit_price * qty

    execute(
        """
        INSERT INTO order_items (
            order_id,
            menu_item_id,
            item_name,
            quantity,
            unit_price,
            total_price
        )
        VALUES (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        )
        """,
        (
            order_id,
            menu_item_id,
            menu_item["name"],
            qty,
            unit_price,
            total_price
        )
    )

    calculate_total(order_id)


def remove_item(order_item_id):

    order_item = fetch_one(
        """
        SELECT *
        FROM order_items
        WHERE id = %s
        """,
        (order_item_id,)
    )

    if not order_item:
        return False

    execute(
        """
        DELETE FROM order_items
        WHERE id = %s
        """,
        (order_item_id,)
    )

    calculate_total(
        order_item["order_id"]
    )

    return True


def update_quantity(    order_item_id,    qty):

    order_item = fetch_one(
        """
        SELECT *
        FROM order_items
        WHERE id = %s
        """,
        (order_item_id,)
    )

    if not order_item:
        return False

    total_price = (
        float(order_item["unit_price"])
        * qty
    )

    execute(
        """
        UPDATE order_items
        SET
            quantity = %s,
            total_price = %s
        WHERE id = %s
        """,
        (
            qty,
            total_price,
            order_item_id
        )
    )

    calculate_total(
        order_item["order_id"]
    )

    return True



def get_order_items(order_id):

    return fetch_all(
        """
        SELECT *
        FROM order_items
        WHERE order_id=%s
        ORDER BY id
        """,
        (order_id,)
    )    


# ======================
# ORDER TOTALS
# ======================

def calculate_total(order_id):

    result = fetch_one(
        """
        SELECT
            COALESCE(
                SUM(total_price),
                0
            ) AS total
        FROM order_items
        WHERE order_id = %s
        """,
        (order_id,)
    )

    total = result["total"]

    execute(
        """
        UPDATE orders
        SET total_amount = %s
        WHERE id = %s
        """,
        (
            total,
            order_id
        )
    )

    return total



# ======================
# ORDER STATUS
# ======================

def mark_paid(order_id):

    order = fetch_one(
        """
        SELECT *
        FROM orders
        WHERE id = %s
        """,
        (order_id,)
    )

    if not order:
        return False

    execute(
        """
        UPDATE orders
        SET status='paid'
        WHERE id=%s
        """,
        (order_id,)
    )

    execute(
        """
        INSERT INTO payments (
            order_id,
            amount,
            payment_method,
            payment_status
        )
        VALUES (
            %s,
            %s,
            'cash',
            'paid'
        )
        """,
        (
            order_id,
            order["total_amount"]
        )
    )

    open_table(
        order["table_id"]
    )

    return True


def update_order_status(    order_id,    status):

    execute(
        """
        UPDATE orders
        SET status = %s
        WHERE id = %s
        """,
        (
            status,
            order_id
        )
    )

    return True


def cancel_order(order_id):

    order = get_order_by_id(order_id)

    if not order:
        return False

    execute(
        """
        UPDATE orders
        SET status='cancelled'
        WHERE id=%s
        """,
        (order_id,)
    )

    open_table(order["table_id"])

    return True


def can_modify_order(order_id):

    order = get_order_by_id(
        order_id
    )

    if not order:
        return False

    return order["status"] == "pending"  