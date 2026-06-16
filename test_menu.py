from services.menu import (
    get_menu,
    get_menu_item,
    search_menu,
    get_categories
)

print("===== MENU =====")
print(get_menu())

print("\n===== ITEM =====")
print(get_menu_item(1))

print("\n===== SEARCH =====")
print(search_menu("coffee"))

print("\n===== CATEGORIES =====")
print(get_categories())