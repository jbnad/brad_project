import MySQLdb
import csv
import sys
from sql import queries 

input_file = sys.argv[1]


mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='ben_test2')
cursor = mydb.cursor()

csv_data = csv.reader(file(input_file))

"""
sudo /usr/local/mysql/support-files/mysql.server start
Create table real_estate (`id` int(11) NOT NULL AUTO_INCREMENT Primary Key,mls_number int UNIQUE,class varchar(40),building_type varchar(40), area varchar(40),price int,address varchar(40), city varchar(40),state varchar(10),status varchar(40),zoning varchar(20),days_on_market int);
Create table real_estate (mls_number int,class varchar(40),days_on_market int);
"""

#skip header
csv_data.next()

import pdb
#pdb.set_trace()
import re

for row in csv_data:
    price=int(re.sub('(,|\$)','',row[6]))
    zoning=row[12] if row[12] else 0
    #to_load = queries["add_row_dup2"] %(price)
    to_load = queries["add_row_dup3"] %(int(row[2]),row[3],row[4],row[5],price,row[7],row[8],row[9],row[10],zoning,int(row[13]),price, int(row[13]))
    #print to_load
    cursor.execute(to_load)

mydb.commit()
cursor.close()
