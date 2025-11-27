import sqlite3
DB_PATH = "DB.db"
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

A = 101 # "T на сливе подп/в с ДПТС №1 ,°С"
B = 90 # "T исх/в на ДПТС ,°С"

cursor.execute(f"""
    SELECT *
    FROM dpts1
    WHERE "10NDF91CT001" > {A} AND
          "10NDF64CT001" > {B}
    ORDER BY "time" DESC
    LIMIT 10
""")

rows = cursor.fetchall()  # получаем все строки
for row in rows:
    print(row)  # печатаем каждую строку
conn.commit()
conn.close()



