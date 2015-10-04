import MySQLdb as sqldb
from sql import queries
from datetime import datetime
from dateutil import tz

db = sqldb.connect("localhost","root","","main")
cursor = db.cursor()

query_get_timestamp =  queries["get_latest_timestamp"]

cursor.execute(query_get_timestamp)
result_time = cursor.fetchone()[0]
print result_time


from_zone = tz.gettz('UTC')
to_zone = tz.gettz('America/Los_Angeles')

result_time2 = result_time.replace(tzinfo = from_zone)

result_time3 = result_time2.astimezone(to_zone)

a = result_time3.strftime('%Y-%m-%d %H-%M-%S')
print type(a)

#create table
#my_query = queries["create_table"]
#cursor.execute(my_query)
#cursor.close()

#update deleted row
#mls_ids = [40702587,407086961,40709876,40712696]
#mls_ids_conv = ", ".join([str(x) for x in mls_ids])
#my_query = queries["delete_row"] %mls_ids_conv
#cursor.execute(my_query)
#db.commit()
#cursor.close()

#select all
#cursor.execute('select * from homes;')
#results = cursor.fetchall()
#print results

#add row
#my_query = queries["add_row"]
#my_query2 = my_query %(1,100000)
#cursor.execute(my_query2)
#db.commit()
