import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print('Connection to MySQL DB successful')
    except Error as e:
        print(f'The error "{e}" occurred')

    return connection

def execute_query(connection, query, params=None):
    cursor = connection.cursor()
    try:
        if params:
            cursor.execute(query, params)  # Use the params argument
        else:
            cursor.execute(query)  # Handle queries with no parameters
        connection.commit()
        print('Query executed successfully')
    except Error as e:
        print(f'The error "{e}" occurred')
    finally:
        cursor.close()

def execute_read_query(connection, query, params=None):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        if params:
            cursor.execute(query, params)  # Execute query with parameters if provided
        else:
            cursor.execute(query)  # Execute query without parameters if not provided
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f'The error "{e}" occurred')
    finally:
        cursor.close()
