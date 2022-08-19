from mysql_connection import connection, cursor


def create(name, age, email, status):
    sql = 'INSERT INTO clients (name, age, email, status) ' \
          'VALUES (%s, %s, %s, %s)'
    arg = (name, age, email, status)
    cursor.execute(sql, arg)
    connection.commit()


def read():
    sql = 'SELECT * from clients'
    cursor.execute(sql)
    data = cursor.fetchall()
    return data


def update(name, age, email, status, id):
    sql = 'UPDATE clients SET name = %s, age = %s, email = %s, status = %s WHERE id = %s'
    data = (name, age, email, status, id)
    cursor.execute(sql, data)
    connection.commit()
