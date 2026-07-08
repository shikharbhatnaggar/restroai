import streamlit as st

from services.orders import (
    get_all_orders,
    get_order_by_id,
    get_order_items,
    update_order_status,
    mark_paid,
    cancel_order
)

# Inject custom CSS to hide the top header bar
hide_bar_style = """
    <style>
    header[data-testid="stHeader"] {
        visibility: hidden;
        height: 0%;
    }

    /* Hide the bottom "Manage app" toolbar and default footer */
    [data-testid="stToolbar"] {
        visibility: hidden !important;
    }
    footer {
        visibility: hidden !important;
    }
    </style>
"""
st.markdown(hide_bar_style, unsafe_allow_html=True)

st.title("📋 Orders")

orders = get_all_orders()

if not orders:
    st.warning("No orders found")
    st.stop()


# LEFT / RIGHT LAYOUT
col1, col2 = st.columns([1, 2])

with col1:

    selected_order = st.selectbox(
        "Select Order",
        orders,
        format_func=lambda x:
            f"Table {x['table_no']} | {x['status']} | ₹{x['total_amount']}"
    )

with col2:

    order = get_order_by_id(
        selected_order["id"]
    )

    st.subheader(
        f"Order: {order['order_no']}"
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Table",
            order["table_no"]
        )

    with c2:
        st.metric(
            "Status",
            order["status"]
        )

    with c3:
        st.metric(
            "Total",
            f"₹ {order['total_amount']}"
        )

    st.divider()

    items = get_order_items(
        order["id"]
    )

    st.subheader("Order Items")

    st.dataframe(
        items,
        use_container_width=True
    )

    st.divider()

    st.subheader("Actions")

    status = st.selectbox(
        "Change Status",
        [
            "pending",
            "preparing",
            "ready"
        ],
        index=0
    )

    col_a, col_b, col_c = st.columns(3)

    with col_a:

        if st.button("Update Status"):

            update_order_status(
                order["id"],
                status
            )

            st.success(
                "Status Updated"
            )

            st.rerun()

    with col_b:

        if st.button("Mark Paid"):

            mark_paid(
                order["id"]
            )

            st.success(
                "Order Paid"
            )

            st.rerun()

    with col_c:

        if st.button("Cancel Order"):

            cancel_order(
                order["id"]
            )

            st.success(
                "Order Cancelled"
            )

            st.rerun()
