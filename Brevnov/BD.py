import psycopg2

print('Введите номер авиакомпании и ее имя через строчку')
a = input()
b = input()
conn = psycopg2.connect(dbname="amogus", user="postgres", password="111111", host="localhost")
cursor = conn.cursor()
cursor.execute("INSERT INTO airplanes (id, name) VALUES (a, b)")

conn.commit()
print('Сделано')

cursor.close()
conn.close()
