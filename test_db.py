from database import fetch_one

result = fetch_one("SELECT 1 AS test")

print(result)