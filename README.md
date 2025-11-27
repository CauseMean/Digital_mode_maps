# Digital_mode_maps


дописать дорасчёты и проверку на реливантность
(False для неправдоподобных значений параметров)







tag_codes = list(DPTS_1.keys())

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# формируем SQL для вставки одной строки
columns = ", ".join(['"time"'] + [f'"{c}"' for c in tag_codes])
placeholders = ", ".join(["?"] * (len(tag_codes) + 1))
sql = f'INSERT INTO dpts1 ({columns}) VALUES ({placeholders})'

"""
# вставка 8640 пустых строк
for _ in range(8640):
    values = [None] + [None] * len(tag_codes)
    cursor.execute(sql, values)
"""
conn.commit()
conn.close()








conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# обновляем значение
cursor.execute(f"""
    UPDATE dpts1
    SET "{columns}" = ?
    WHERE "time" = ?
""", (new_value, time_value))

conn.commit()
conn.close()

✅ Пояснения: