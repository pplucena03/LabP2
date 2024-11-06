import psycopg2

def start_connection():
    try:
        conn = psycopg2.connect(
            dbname='Atividade AV3 Wagner',
            user='postgres',
            password='pp1234',
            host='localhost',
            port='5432'
        )

        return conn
    
    except Exception as e:
        print(f'ERROR: {e}')
        return None
    