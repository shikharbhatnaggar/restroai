import streamlit as st

from services.orders import (
    get_active_order,
    get_order_items,
    can_modify_order,
    remove_item
)


import streamlit as st

from services.orders import (
    get_active_order,
    get_order_items,
    can_modify_order
)



def render_order_summary(table):

    order = get_active_order(
        table["id"]
    )

    if not order:
        return

    items = get_order_items(
        order["id"]
    )

    st.subheader("📋 Current Order")

    with st.container(border=True):

        col1, col2 = st.columns([3, 1])

        with col1:
            st.write(
                f"**Order:** {order['order_no']}"
            )

        with col2:
            st.write(
                f"**{order['status'].upper()}**"
            )

        st.divider()

        total = 0


        for item in items:

            total += float(item["total_price"])

            col1, col2, col3, col4 = st.columns([4, 1, 2, 1])

            with col1:
                st.write(item["item_name"])

            with col2:
                st.write(f"x{item['quantity']}")

            with col3:
                st.write(f"₹{item['total_price']}")

            with col4:

                if can_modify_order(order["id"]):

                    if st.button(
                        "❌",
                        key=f"rm_{item['id']}"
                    ):

                        remove_item(item["id"])

                        st.rerun()

        st.divider()

        st.metric(
            "Order Total",
            f"₹ {total}"
        )

        if can_modify_order(
            order["id"]
        ):
            st.success(
                "You can still modify this order."
            )
        else:
            st.warning(
                "Order can no longer be modified."
            )