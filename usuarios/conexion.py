import mysql.connector

def conectar():
    #conexion a database
    database = mysql.connector.connect(
        host = "localhost",
        user="tester",
        passwd="tester",
        database = "console_app_python",
        port="3306"
    )

    cursor = database.cursor(buffered=True)

    return[database,cursor]