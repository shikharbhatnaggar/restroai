from services.orders import *

order_id = create_order(5)

add_item(order_id, 1, 2)
add_item(order_id, 2, 1)

print(
    get_active_order(5)
)

print(
    get_order_items(order_id)
)

print(
    calculate_total(order_id)
)