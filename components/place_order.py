import streamlit as st

from services.orders import (
    create_order,
    get_active_order,
    add_item
)


def place_order(table):

    print("PLACE ORDER CLICKED")

    print(table)

    print(st.session_state.cart)

    if not st.session_state.cart:

        st.warning(
            "Cart is empty"
        )

        return

    active_order = get_active_order(
        table["id"]
    )

    print("ACTIVE ORDER")
    print(active_order)

    if active_order:

        order_id = active_order["id"]

    else:

        order_id = create_order(
            table["id"]
        )

    print("ORDER ID")
    print(order_id)

    for item in st.session_state.cart:

        add_item(
            order_id,
            item["id"],
            item["qty"]
        )

    st.session_state.cart = []

    st.success(
        f"Order #{order_id} submitted successfully"
    )

    return order_id