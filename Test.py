import pandas as pd
import sqlite3

# читаем файл
df = pd.read_excel("rep_2025_11_6_13_39_37.xlsx")
DPTS_1 = {
    "10NDF64CF001" : "F исх/в на ДПТС ,т/ч", # 5
    "10NDF64CT001" : "T исх/в на ДПТС ,°С", # 6
    "10NDF64CP001" : "P исх/в после ПИВ ,МПа", # 4

}
value = df.iloc[33, 2]  # индексация с нуля
print(value)

DB_PATH = "DB.db"


conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS dpts1 (
        time TEXT PRIMARY KEY,
        "10NDF64CF001" REAL,
        "10NDP64CF001" REAL,
        "10NDT64CF001" REAL
    )
""")
conn.commit()
conn.close()
