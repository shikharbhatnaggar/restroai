import streamlit as st

from components.table_verification import (
    render_table_verification
)

from components.menu_view import (
    render_menu
)

from components.cart import (
    init_cart,
    render_cart
)

from components.order_summary import (
    render_order_summary
)

st.set_page_config(
    page_title="Restaurant OS",
    layout="wide"
)

st.title("🍽 Restaurant OS")

table = render_table_verification()

init_cart()

render_order_summary(
    table
)

render_menu()

render_cart()