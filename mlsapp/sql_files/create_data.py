import MySQLdb
import csv
import sys
from sql import queries 
import re

input_file = sys.argv[1]

possible_hosts = ['ec2-54-152-43-137.compute-1.amazonaws.com','localhost']
my_host = possible_hosts[1] 

mydb = MySQLdb.connect(host=my_host,
    user='root',
    passwd='',
    db='main')
cursor = mydb.cursor()


#create table
try:
    create_table_query = queries['create_table']
    cursor.execute(create_table_query)
    mydb.commit()
except Exception as e:
    print str(e),type(e)
    sys.exit()

#create table
try:
    create_table_query = queries['create_table_update_time']
    cursor.execute(create_table_query)
    mydb.commit()
except Exception as e:
    print str(e),type(e)
    sys.exit()





#insert into real_estate table
csv_data = csv.reader(file(input_file))

#gets header and skips first row
headers = csv_data.next()

required_headers = ['Photo', 'Picture', 'MLS Number', 'Class', 'Building Type', 'Area', 'Price', 'Address', 'City', 'State', 'Status', 'Radar ID', 'Zoning', 'Days On Market']
if headers != required_headers:
    print 'Wrong Headers.  I need the following in order:'
    print 'Photo, Picture, MLS Number, Class, Building Type, Area, Price, Address, City, State, Status, Radar ID, Zoning, Days On Market' 



mystring = "Insert into real_estate values"
mystring2 = " on Duplicate Key Update days_on_market=values(days_on_market), last_updated=now(), price=values(price);"
mystring0 = []

for row in csv_data:
    price=int(re.sub('(,|\$)','',row[6]))
    zoning=row[12] if row[12] else 0
    mystring0.append(queries["insert_update"] %(int(row[2]),row[3],row[4],row[5],price,row[7],row[8],row[9],row[10],zoning,int(row[13])))

final = ",".join(mystring0)
 
final1 = mystring + final + mystring2
cursor.execute(final1)
mydb.commit()



#update time table
insert_update_time_query = queries['insert_into_update_time']
cursor.execute(insert_update_time_query)
mydb.commit()



cursor.close()


print 'done'