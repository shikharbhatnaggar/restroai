import streamlit as st

from database import fetch_one, fetch_all

from services.dashboard import (
    get_open_tables,
    get_reserved_tables
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

st.title("📊 Dashboard")

open_tables = get_open_tables()
reserved_tables = get_reserved_tables()

revenue = fetch_one("""
SELECT COALESCE(
    SUM(total_amount),
    0
) total
FROM orders
WHERE status='paid'
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Open Tables",
        open_tables
    )

with col2:
    st.metric(
        "Reserved Tables",
        reserved_tables
    )

with col3:
    st.metric(
        "Revenue",
        f"₹ {revenue['total']}"
    )

tables = fetch_all("""
SELECT *
FROM restaurant_tables
ORDER BY table_no
""")

st.subheader("Tables")

for table in tables:

    if table["status"] == "open":
        st.success(
            f"Table {table['table_no']} - Open"
        )
    else:
        st.error(
            f"Table {table['table_no']} - Reserved"
        )
