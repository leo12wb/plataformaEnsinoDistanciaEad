from database.database import get_db_connection
from models.modules import Modules

def create(module: Modules):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO modules (title, description) VALUES (%s, %s)",
        (module.title, module.description)
    )

    module_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()
    return Modules(id=module_id, **module.dict(exclude={"id"}))

def readAll():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM modules")
    modules = cursor.fetchall()
    cursor.close()
    connection.close()
    return [Modules(**module) for module in modules]

def readOne(id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM modules WHERE id = %s", (id,))
    module = cursor.fetchone()
    cursor.close()
    connection.close()
    return module

def update(id: int, module: Modules):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE modules SET title = %s, description = %s WHERE id = %s",
        (module.title, module.description, id)
    )

    module_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()
    return Modules(id=module_id, **module.dict(exclude={"id"}))

def delete(id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM modules WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
