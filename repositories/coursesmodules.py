from database.database import get_db_connection
from models.coursesmodules import Coursesmodules

def create(coursesmodules: Coursesmodules):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO coursesmodules (course_Id, module_Id, 	ordenation) VALUES (%s, %s, %s)",
        (coursesmodules.course_Id, coursesmodules.module_Id, coursesmodules.ordenation)
    )

    coursesmodules_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()
    return Coursesmodules(id=coursesmodules_id, **coursesmodules.dict(exclude={"id"}))

def readAll():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM coursesmodules")
    coursesmodules = cursor.fetchall()
    cursor.close()
    connection.close()
    return [Coursesmodules(**coursesmodule) for coursesmodule in coursesmodules]

def readOne(id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM coursesmodules WHERE id = %s", (id,))
    coursesmodules = cursor.fetchone()
    cursor.close()
    connection.close()
    return coursesmodules

def update(id: int, coursesmodules: Coursesmodules):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE coursesmodules SET course_Id = %s, module_Id = %s, ordenation = %s WHERE id = %s",
        (coursesmodules.course_Id, coursesmodules.module_Id, coursesmodules.ordenation, id)
    )

    coursesmodules_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()
    return Coursesmodules(id=coursesmodules_id, **coursesmodules.dict(exclude={"id"}))

def delete(id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM coursesmodules WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
