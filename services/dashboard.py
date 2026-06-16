from database import fetch_one


def get_open_tables():

    result = fetch_one("""
    SELECT COUNT(*) total
    FROM restaurant_tables
    WHERE status='open'
    """)

    return result["total"]


def get_reserved_tables():

    result = fetch_one("""
    SELECT COUNT(*) total
    FROM restaurant_tables
    WHERE status='reserved'
    """)

    return result["total"]


def get_total_revenue():

    result = fetch_one("""
    SELECT
        COALESCE(
            SUM(total_amount),
            0
        ) total
    FROM orders
    WHERE status='paid'
    """)

    return result["total"]