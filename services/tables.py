from database import fetch_one, fetch_all, execute


def get_table_by_number(table_no):
    """
    Get a table by its number.
    """

    return fetch_one(
        """
        SELECT *
        FROM restaurant_tables
        WHERE table_no = %s
        """,
        (table_no,)
    )


def verify_table(table_no, verification_code):
    """
    Verify table number and verification code.
    Returns table record if valid else None.
    """

    return fetch_one(
        """
        SELECT *
        FROM restaurant_tables
        WHERE table_no = %s
        AND verification_code = %s
        """,
        (
            table_no,
            verification_code
        )
    )


def reserve_table(table_id):
    """
    Mark table as reserved.
    """

    execute(
        """
        UPDATE restaurant_tables
        SET status = 'reserved'
        WHERE id = %s
        """,
        (table_id,)
    )

    return True


def open_table(table_id):
    """
    Mark table as open.
    """

    execute(
        """
        UPDATE restaurant_tables
        SET status = 'open',
            active_order_id = NULL
        WHERE id = %s
        """,
        (table_id,)
    )

    return True


def get_all_tables():
    """
    Get all tables.
    """

    return fetch_all(
        """
        SELECT *
        FROM restaurant_tables
        ORDER BY table_no ASC
        """
    )    



def get_table_by_id(table_id):

    return fetch_one(
        """
        SELECT *
        FROM restaurant_tables
        WHERE id = %s
        """,
        (table_id,)
    )        


def get_table_counts():

    return fetch_one(
        """
        SELECT
            SUM(CASE WHEN status='open' THEN 1 ELSE 0 END) AS open_tables,
            SUM(CASE WHEN status='reserved' THEN 1 ELSE 0 END) AS reserved_tables
        FROM restaurant_tables
        """
    )