import pandas as pd
import sqlite3
import KKS_DPTS_1

DB_PATH = "DB.db"
df = pd.read_excel("DPTS1 — копия.xlsx")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# создаём таблицу с колонками из тегов
columns = ",\n".join([f'"{code}" REAL' for code in KKS_DPTS_1.DPTS_1])
cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS dpts1 (
        time TEXT,
        {columns}
    )
""")

# выбираем строку
values = df.iloc[0]  # пример: первая строка


# вставляем только числа
data = [values[code] for code in KKS_DPTS_1.DPTS_1]

placeholders = ", ".join(["?"] * (len(KKS_DPTS_1.DPTS_1) + 1))
cursor.execute(f"INSERT INTO dpts1 VALUES ({placeholders})", data)

conn.commit()
conn.close()