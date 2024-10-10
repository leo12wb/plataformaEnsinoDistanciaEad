from database.database import get_db_connection
from models.courses import Courses 

def create(course: Courses):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO courses (title, description, start_date, end_date, status) VALUES (%s, %s, %s, %s, %s)",
        (course.title, course.description, course.start_date, course.end_date, course.status)
    )

    course_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()
    return Courses(id=course_id, **course.dict(exclude={"id"}))

def readAll():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()
    cursor.close()
    connection.close()
    return [Courses(**course) for course in courses]

def readOne(id: int):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM courses WHERE id = %s", (id,))
    course = cursor.fetchone()
    cursor.close()
    connection.close()
    return course

def update(id: int, course: Courses):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE courses SET title = %s, description = %s, start_date = %s, end_date = %s, status = %s WHERE id = %s",
        (course.title, course.description, course.start_date, course.end_date, course.status, id)
    )

    course_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()
    return Courses(id=course_id, **course.dict(exclude={"id"}))

def delete(id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM courses WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()



# from database.database import get_db_connection

# def create(name: str, price: float):
#     connection = get_db_connection()
#     cursor = connection.cursor()
#     cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (name, price))
#     connection.commit()
#     cursor.close()
#     connection.close()

# def readAll():
#     connection = get_db_connection()
#     cursor = connection.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM products")
#     products = cursor.fetchall()
#     cursor.close()
#     connection.close()
#     return products

# def readOne(product_id: int):
#     connection = get_db_connection()
#     cursor = connection.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
#     product = cursor.fetchone()
#     cursor.close()
#     connection.close()
#     return product

# def update(product_id: int, name: str, price: float):
#     connection = get_db_connection()
#     cursor = connection.cursor()
#     cursor.execute("UPDATE products SET name = %s, price = %s WHERE id = %s", (name, price, product_id))
#     connection.commit()
#     cursor.close()
#     connection.close()

# def delete(product_id: int):
#     connection = get_db_connection()
#     cursor = connection.cursor()
#     cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
#     connection.commit()
#     cursor.close()
#     connection.close()
