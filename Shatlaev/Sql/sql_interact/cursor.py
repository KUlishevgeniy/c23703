from .connection import connection

cursor = connection.cursor()
def add_rows(id_company: int, name: str) -> None:
    insert_query = f'''INSERT INTO public.aviacompany(
	id_company, name)
	VALUES ('{id_company}', '{name}');'''
    cursor.execute(insert_query)
    connection.commit()

def select_rows() -> list:
    cursor.execute(f'''SELECT * FROM public.aviacompany;''')
    return cursor.fetchall()

def update_rows(set_params: str, condition: str) -> None:
    cursor.execute(f'''UPDATE public.aviacompany SET {set_params} WHERE {condition};''')
    connection.commit()