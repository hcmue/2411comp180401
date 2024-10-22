import pymysql
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost', user='root', password='',
                             database='2411comp180401',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `lop` (`malop`, `tenlop`, CVHT) VALUES (%s, %s, %s)"
        cursor.execute(sql, ('48.01.CNTT.B', '48.01.CNTT.B', 'XYZ'))

    connection.commit()

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM `lop`")
        result = cursor.fetchall()
        for rs in result:
            print(rs)