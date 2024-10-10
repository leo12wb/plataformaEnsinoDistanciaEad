from database.database import get_db_connection
from models.disciplines import Disciplines

def create(disciplines: Disciplines):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO disciplines (title, description) VALUES (%s, %s)",
        (disciplines.title, disciplines.description)
    )

    disciplines_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()
    return Disciplines(id=disciplines_id, **disciplines.dict(exclude={"id"}))

def readAll():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM disciplines")
    disciplines = cursor.fetchall()
    cursor.close()
    connection.close()
    return [Disciplines(**discipline) for discipline in disciplines]

def readOne(id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM disciplines WHERE id = %s", (id,))
    discipline = cursor.fetchone()
    cursor.close()
    connection.close()
    return discipline

def update(id: int, disciplines: Disciplines):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE disciplines SET title = %s, description = %s WHERE id = %s",
        (disciplines.title, disciplines.description, id)
    )

    disciplines_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()
    return Disciplines(id=disciplines_id, **disciplines.dict(exclude={"id"}))

def delete(id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM disciplines WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
