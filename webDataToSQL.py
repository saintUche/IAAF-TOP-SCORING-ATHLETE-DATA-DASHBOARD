from sqlalchemy import create_engine
import pymysql
from scraper import all_athletes


table_name = "Rankings"

engine = create_engine("mysql://{user}:{pw}@localhost:3306/{db}".format(user="root", pw="", db="eventRankings"))
db_connection = engine.connect()

try:
    all_athletes.to_sql(table_name, db_connection, if_exists='append', index=False)

except ValueError as vx:
    print(vx)
    print("did not connect")

except Exception as ex:
    print(ex)
    print("did not connect")

else:
    ("Table %s created successufullt." %table_name)

finally:
    db_connection.close()
