import streamlit as st

from services.tables import (
    get_table_by_number,
    verify_table
)


def render_table_verification():

    params = st.query_params

    table_no = params.get("table")

    if not table_no:

        st.error(
            "Invalid QR Code"
        )

        st.stop()

    table = get_table_by_number(
        int(table_no)
    )

    if not table:

        st.error(
            "Table not found"
        )

        st.stop()

    st.success(
        f"Table {table['table_no']}"
    )

    if "verified" not in st.session_state:
        st.session_state.verified = False

    if not st.session_state.verified:

        code = st.text_input(
            "Verification Code"
        )

        if st.button("Verify"):

            verified = verify_table(
                table["table_no"],
                code
            )

            if verified:

                st.session_state.verified = True

                st.session_state.table = table

                st.rerun()

            else:

                st.error(
                    "Invalid Code"
                )

        st.stop()

    return table