import MySQLdb
import csv
import sys
from sql import queries 

input_file = sys.argv[1]

mydb = MySQLdb.connect(host='ec2-54-152-43-137.compute-1.amazonaws.com',
    user='root',
    passwd='',
    db='main')
cursor = mydb.cursor()

csv_data = csv.reader(file(input_file))


#skip header
csv_data.next()

import pdb
#pdb.set_trace()
import re

mystring = "Insert into real_estate values"
mystring2 = " on Duplicate Key Update days_on_market=values(days_on_market), last_updated=now(), price=values(price);"
mystring0 = []

for row in csv_data:
    price=int(re.sub('(,|\$)','',row[6]))
    zoning=row[12] if row[12] else 0
                                   #(`id`,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s', '%s', '', '', '0', '0', '')
    mystring0.append(queries["testyo2"] %(int(row[2]),row[3],row[4],row[5],price,row[7],row[8],row[9],row[10],zoning,int(row[13])))
    #cursor.execute(to_load)

final = ",".join(mystring0)
 
final1 = mystring + final + mystring2
cursor.execute(final1)
mydb.commit()
cursor.close()

"""
#ACTUAL...MUST KEEP

for row in csv_data:
    price=int(re.sub('(,|\$)','',row[6]))
    zoning=row[12] if row[12] else 0
    to_load = queries["add_row_dup2"] %(int(row[2]),row[3],row[4],row[5],price,row[7],row[8],row[9],row[10],zoning,int(row[13]),price, int(row[13]))
    cursor.execute(to_load)
 
mydb.commit()
cursor.close()

"""






"""
params=[]
for row in csv_data:
    price=str(int(re.sub('(,|\$)','',row[6])))
    zoning=row[12] if row[12] else 0
    values = (str(int(row[2])),row[3],row[4],row[5],price,row[7],row[8],row[9],row[10],zoning,str(int(row[13])),price, str(int(row[13])))
    params.append(values)
import pdb
pdb.set_trace()


query = queries["testing"] 
cursor.executemany(query, params)

mydb.commit()
cursor.close()
"""
