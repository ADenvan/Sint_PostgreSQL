import psycopg2
from config import host, user, password, db_name

try:
  connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
  )
  with connection.cursor() as cur:
    cur.execute(
      "SELECT version();"
    )
    print(f"Server version: {cur.fetchone()}")
except Exception as _ex:
  print("[INFO] Error while working with postgresql", _ex)
finally:
  if connection:
    connection.close()
    print("[INFO] PostgresSql connection closed") 