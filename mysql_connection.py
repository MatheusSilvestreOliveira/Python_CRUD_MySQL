import pymysql.cursors

connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    db='clients',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = connection.cursor()
