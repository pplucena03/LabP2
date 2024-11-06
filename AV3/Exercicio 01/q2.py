from services import start_connection

print("\n-------- Questão 2 --------")

conn = start_connection()
try:
    cursor = conn.cursor()
    query = 'SELECT titulo FROM jogos ORDER BY titulo'
    cursor.execute(query)
    resultado = cursor.fetchall()
    for i in range(len(resultado)):
        print(resultado[i])

except Exception as e:
    print(f"ERROR: {e}")

finally:
    cursor.close()
    conn.close()