import streamlit as st

from services.menu import get_menu

from components.cart import (
    add_to_cart
)


def render_menu():

    menu_items = get_menu()

    st.subheader("Menu")

    for item in menu_items:

        col1, col2 = st.columns([4, 1])

        with col1:

            st.write(
                f"**{item['name']}**"
            )

            st.caption(
                f"₹ {item['price']}"
            )

        with col2:

            if st.button(
                "Add",
                key=f"add_{item['id']}"
            ):

                add_to_cart(item)

                st.rerun()