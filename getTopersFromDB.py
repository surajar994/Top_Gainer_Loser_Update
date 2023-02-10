import mysql.connector
from datetime import date

table_name = "topers_test"


def get_existing_records_count(on_date):
    connection = mysql.connector.connect(user='root', password='Trader@01', host='127.0.0.1',
                                        database='stockRecoDB')
    cursor = connection.cursor()
    qry = f"select count(id) from {table_name} where Date='{on_date}' and position='G';"
    cursor.execute(qry)
    records = cursor.fetchall()
    return records[0][0]
    connection.close()
