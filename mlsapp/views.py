from django.shortcuts import render

from django.utils import timezone
from django.http import HttpResponse,HttpResponseRedirect

import MySQLdb as sqldb
from sql_files.sql import queries
import django.db

from datetime import datetime
from dateutil import tz
from_zone = tz.gettz('UTC')
to_zone = tz.gettz('America/Los_Angeles')


#db = sqldb.connect("localhost","root","","main")


def getsql(sql):
    dbyo = sqldb.connect("localhost","root","","main")
    cursor = dbyo.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    dbyo.close()
    return result

def commmitsql(sql):
    dbyo = sqldb.connect("localhost","root","","main")
    cursor = dbyo.cursor()
    cursor.execute(sql)
    dbyo.commit()
    cursor.close()
    dbyo.close()


def notes(request):
    if request.method == 'POST':
        print request.POST['mls_id']
        print request.POST['note_input']
    return HttpResponse('whatevs from notes')        

def delete_rows(request):
    to_delete = []
    for i in request.POST.keys(): 
        to_delete.append(request.POST.getlist(i)[1])
    

    mls_ids_conv = ", ".join([str(x) for x in to_delete])

    my_query = queries["delete_row"] %mls_ids_conv
    
    commmitsql(my_query)
    #cursor = db.cursor()
    #cursor.execute(my_query)
    #db.commit()
    #cursor.close()


    return HttpResponse('whatevs')

def un_watch_and_delete_and_rows(request):
    to_delete_unwatch = []
    for i in request.POST.keys(): 
        to_delete_unwatch.append(request.POST.getlist(i)[1])

    mls_ids_conv = ", ".join([str(x) for x in to_delete_unwatch])

    my_query = queries["delete_unwatch_row"] %mls_ids_conv

    commmitsql(my_query)
    #cursor = db.cursor()
    #cursor.execute(my_query)
    #db.commit()
    #cursor.close()

    return HttpResponse('whatevs')


def undelete(request):

    to_undelete = []
    for i in request.POST.keys(): 
        to_undelete.append(request.POST.getlist(i)[1])

    mls_ids_conv = ", ".join([str(x) for x in to_undelete])

    my_query = queries["undelete_row"] %mls_ids_conv
    
    commmitsql(my_query)
    #cursor = db.cursor()
    #cursor.execute(my_query)
    #db.commit()
    #cursor.close()


    return HttpResponse('whatevs')



def add_watch_list(request):
    to_add = []
    for i in request.POST.keys(): 
        to_add.append(request.POST.getlist(i)[1])

    mls_ids_conv = ", ".join([str(x) for x in to_add])

    my_query = queries["add_watch_list"] %mls_ids_conv

    commmitsql(my_query)
    #cursor = db.cursor()
    #cursor.execute(my_query)
    #db.commit()
    #cursor.close()


    return HttpResponse('whatevs')

def remove_watch_list(request):
    to_add = []
    for i in request.POST.keys(): 
        to_add.append(request.POST.getlist(i)[1])


    mls_ids_conv = ", ".join([str(x) for x in to_add])

    my_query = queries["remove_watch_list"] %mls_ids_conv
    
    commmitsql(my_query)
    #cursor = db.cursor()
    #cursor.execute(my_query)
    #db.commit()
    #cursor.close()


    return HttpResponse('whatevs')


def update_note(request):
 
    mls_id, note_input = request.POST["mls_id"], request.POST["note_input"]
    my_query = queries["update_note"] %(note_input, mls_id)
    
    commmitsql(my_query)
    #cursor = db.cursor()
    #cursor.execute(query)
    #db.commit()
    #cursor.close()
    return HttpResponse('whatevs')

def watch_list(request):
    query = queries["get_watchlist"]

    result = getsql(query)
    #cursor = db.cursor()
    #cursor.execute(query)
    #result = cursor.fetchall()
    #cursor.close()

    if not result:
        result = [(),]

    return render(request, 'mlsapp/watch_list.html', {'mydata': result})


def deleted(request):
    query = queries["get_deleted"]

    result = getsql(query)
    #cursor = db.cursor()
    #cursor.execute(query)
    #result = cursor.fetchall()
    #cursor.close()

    if not result:
        result = [(),]

    return render(request, 'mlsapp/deleted.html', {'mydata': result})



def get_main(request):
    query = queries["get_not_deleted_not_hotlist"]
    query_get_timestamp =  queries["get_latest_timestamp"]

    #try:
    #    cursor = db.cursor()
    #    cursor.execute(query)
    #    result = cursor.fetchall()
    #    cursor.execute(query_get_timestamp)
    #except (AttributeError, MySQLdb.OperationalError):
    #except:
    #    print 'fail'
    #    db = sqldb.connect("localhost","root","","main")
    #    cursor = db.cursor()
    #    cursor.execute(query)
    #    result = cursor.fetchall()
    #    cursor.execute(query_get_timestamp)
    #import pdb
    #pdb.set_trace()
    result = getsql(query)
    result_time = getsql(query_get_timestamp)

    #import pdb
    #pdb.set_trace()

    result_time = result_time[0][0]
    result_time = result_time.replace(tzinfo = from_zone)
    result_time = result_time.astimezone(to_zone)
    result_time = result_time.strftime('%Y-%m-%d %H:%M:%S')

    #cursor.close()

    return_data = result[:10]

    return render(request, 'mlsapp/data.html', {'mydata': return_data, 'latest_time': result_time})




#def get_main2(request):
    #return HttpResponse("Hello, world. You're at the poll index.")
#    if request.method == 'POST':
#        to_delete=[]
#        for i in request.POST.keys(): 
#            to_delete.append(request.POST.getlist(i))
#        print to_delete
#        return HttpResponse('whatevs')
#
#    else:
#        return render(request,'polls/data.html',{'mydata':
#            [['Smithy','Jonny','j@g',70,'http://whatev', 'a prev', 'long form note'],
#            ['Smithy','Jonny','j@g',70,'http://whatev', 'a prev 2', 'long from note 2']]})

#def form(request):
#    return render(request,'polls/index.html')

#def index(request):
#    return HttpResponse("Hello, world. You're at the poll index.")
