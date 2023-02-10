import mysql.connector
from datetime import date

table_name = "topers_test"


def add_to_db(stock_list):
    for stock in stock_list:
        connection = mysql.connector.connect(user='root', password='xxxxxxxx', host='127.0.0.1',
                                             database='stockRecoDB')
        cursor = connection.cursor()
        today = date.today()
        qry = f'''INSERT INTO {table_name}(Date,symbol,position,percentage,openPrice,highPrice,lowPrice) 
        VALUES(
        "{today}",
        "{stock['symbol']}", 
        "{stock['position']}",
        "{stock['percentage']}", 
        "{stock['openPrice']}", 
        "{stock['highPrice']}", 
        "{stock['lowPrice']}")'''
        cursor.execute(qry)
        connection.commit()
        connection.close()


def format_list(stock_list, position):
    formatter_stock_list = []
    for stock in stock_list:
        stock_data_for_db = {'symbol': stock['symbol'],
                             'position': position,
                             'openPrice': stock['openPrice'],
                             'lowPrice': stock['lowPrice'],
                             'highPrice': stock['highPrice'],
                             'percentage': round(((stock['ltp'] / stock['previousPrice']) - 1) * 100, 2)}
        formatter_stock_list.append(stock_data_for_db)
    return formatter_stock_list
