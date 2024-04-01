import pymysql

def connectBd():
    try:
        connection = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='',
            database='cafe_pp',
            cursorclass=pymysql.cursors.DictCursor
        )
    except Exception as ex:
        print(ex)
    return connection
