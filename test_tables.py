from services.tables import (
    get_table_by_number,
    verify_table,
    reserve_table,
    open_table,
    get_all_tables
)

print("------ Table 5 ------")
print(get_table_by_number(5))

print("\n------ Verify ------")
print(
    verify_table(
        5,
        "T5E3"
    )
)

print("\n------ All Tables ------")
print(get_all_tables())