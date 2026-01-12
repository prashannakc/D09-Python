# import mysql.connector

# db = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="",
#     port=3306,
#     database="meroshare" 
# )



# my_terminal = db.cursor()
# my_terminal.execute("alter table share add (share_name VARCHAR(50), price DECIMAL(10, 2), quantity INT, created_at DATE)")



# # my_terminal.execute("select name, address from learning where id = 1") 
# # result = my_terminal.fetchall()
# # print(result) 
# # for i in result:
# #     print(i[1]) 

# import requests 

# url = "https://www.onlinekhabar.com/smtm/home/trending"

# r = requests.get(url=url)

# if r.status_code == 200:
#     data = r.json()
#     print(data.keys()) 


#CA(for latest price updates)
import requests
import mysql.connector

API_URL = "https://www.onlinekhabar.com/smtm/home/trending"

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="meroshare"
)

cursor = db.cursor()

r = requests.get(API_URL)


if r.ok:
    datas = r.json()["response"]

    sql = """
    INSERT INTO live_stocks
    (ticker, ticker_name, latest_price, points_change, percentage_change, traded_of_mkt_cap)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        latest_price = VALUES(latest_price),
        points_change = VALUES(points_change),
        percentage_change = VALUES(percentage_change),
        traded_of_mkt_cap = VALUES(traded_of_mkt_cap)
    """

    for data in datas:
        values = (
            data["ticker"],
            data["ticker_name"],
            data["latest_price"],
            data["points_change"],
            data["percentage_change"],
            data["traded_of_mkt_cap"]
        )
        cursor.execute(sql, values)

    db.commit()
    
    #for historical data(unupdated) 
    sql = """
    INSERT IGNORE current_stocks
    (ticker, ticker_name, latest_price, points_change, percentage_change, traded_of_mkt_cap)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    for data in datas:
        values = (
            data["ticker"],
            data["ticker_name"],
            data["latest_price"],
            data["points_change"],
            data["percentage_change"],
            data["traded_of_mkt_cap"]
        )
        cursor.execute(sql, values)

    db.commit()

cursor.close()
db.close()

print("Data inserted successfully.")


