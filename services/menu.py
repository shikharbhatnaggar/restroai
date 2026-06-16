from database import fetch_one, fetch_all


def get_menu():
    """
    Get all active menu items.
    """

    return fetch_all(
        """
        SELECT *
        FROM menu_items
        WHERE status = 'active'
        ORDER BY category, name
        """
    )


def get_menu_item(menu_item_id):
    """
    Get single menu item by ID.
    """

    return fetch_one(
        """
        SELECT *
        FROM menu_items
        WHERE id = %s
        """,
        (menu_item_id,)
    )


def search_menu(keyword):
    """
    Search menu items by name, category or description.
    """

    keyword = f"%{keyword}%"

    return fetch_all(
        """
        SELECT *
        FROM menu_items
        WHERE status = 'active'
        AND (
            name LIKE %s
            OR category LIKE %s
            OR description LIKE %s
        )
        ORDER BY category, name
        """,
        (
            keyword,
            keyword,
            keyword
        )
    )


def get_categories():
    """
    Get distinct menu categories.
    """

    return fetch_all(
        """
        SELECT DISTINCT category
        FROM menu_items
        WHERE status = 'active'
        ORDER BY category
        """
    )


def get_menu_by_category(category):

    return fetch_all(
        """
        SELECT *
        FROM menu_items
        WHERE status = 'active'
        AND category = %s
        ORDER BY name
        """,
        (category,)
    )


def get_featured_menu(limit=5):

    return fetch_all(
        """
        SELECT *
        FROM menu_items
        WHERE status = 'active'
        ORDER BY id DESC
        LIMIT %s
        """,
        (limit,)
    )    