import MySQLdb as sqldb
from sql import queries

db = sqldb.connect("localhost","root","","ben_test2")
cursor = db.cursor()

#create table
my_query = queries["create_table"]
cursor.execute(my_query)
cursor.close()

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
