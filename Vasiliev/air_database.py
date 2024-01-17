import psycopg2

a = input('Введите номер авиакомпании:')
b = input('Введите название авиакомпании')
conn = psycopg2.connect(dbname="hamburger", user="postgres", password="111111", host="localhost")
cursor = conn.cursor()
cursor.execute("INSERT INTO airplanes (id, name) VALUES (a, b)")

conn.commit()
print('Сделано')

cursor.close()
conn.close()
