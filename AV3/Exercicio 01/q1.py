from services import start_connection

print("-------- Questão 1 --------")
user_input = input("Digite algo: ")
user_input = f"%{user_input}%"

conn = start_connection()
try:
    cursor = conn.cursor()
    query = 'SELECT titulo, subtitulo FROM jogos WHERE titulo ILIKE %s OR subtitulo ILIKE %s'
    cursor.execute(query, (user_input, user_input))
    resultado = cursor.fetchall()
    for i in range(len(resultado)):
        print(resultado[i])

except Exception as e:
    print(f"ERROR: {e}")

finally:
    cursor.close()
    conn.close()