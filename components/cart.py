import streamlit as st

from components.place_order import (
    place_order
)

from services.orders import (
    get_active_order,
    can_modify_order
)


def init_cart():

    if "cart" not in st.session_state:

        st.session_state.cart = []



def add_to_cart(menu_item):

    for item in st.session_state.cart:

        if item["id"] == menu_item["id"]:

            item["qty"] += 1

            return

    st.session_state.cart.append({
        "id": menu_item["id"],
        "name": menu_item["name"],
        "price": float(menu_item["price"]),
        "qty": 1
    })



def remove_from_cart(menu_item_id):

    st.session_state.cart = [

        item

        for item in st.session_state.cart

        if item["id"] != menu_item_id
    ]



def calculate_cart_total():

    total = 0

    for item in st.session_state.cart:

        total += (
            item["price"]
            * item["qty"]
        )

    return total



def render_cart():

    with st.sidebar:

        st.header("🛒 Cart")

        if not st.session_state.cart:

            st.info("Cart is empty")

            return

        total = 0

        for item in st.session_state.cart:

            line_total = (
                item["price"]
                * item["qty"]
            )

            total += line_total

            col1, col2 = st.columns([4, 1])

            with col1:

                st.write(
                    f"{item['name']} x {item['qty']}"
                )

            with col2:

                if st.button(
                    "❌",
                    key=f"remove_{item['id']}"
                ):

                    remove_from_cart(
                        item["id"]
                    )

                    st.rerun()

        st.divider()

        st.metric(
            "Total",
            f"₹ {total}"
        )

        active_order = get_active_order(
            st.session_state.table["id"]
        )

        can_place_order = True

        if active_order:

            if can_modify_order(
                active_order["id"]
            ):

                st.info(
                    "Items will be added to existing order."
                )

            else:

                can_place_order = False

                st.warning(
                    "Order can no longer be modified."
                )

        else:

            st.info(
                "New order will be created."
            )

        if st.button(
            "Place Order",
            use_container_width=True,
            disabled=not can_place_order
        ):

            place_order(
                st.session_state.table
            )

            st.rerun()