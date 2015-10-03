from django.shortcuts import render

from django.utils import timezone
from django.http import HttpResponse,HttpResponseRedirect

import MySQLdb as sqldb
from sql_files.sql import queries
db = sqldb.connect("localhost","root","","ben_test2")


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
    
    cursor = db.cursor()
    cursor.execute(my_query)
    db.commit()
    cursor.close()


    return HttpResponse('whatevs')

def un_watch_and_delete_and_rows(request):
    to_delete_unwatch = []
    for i in request.POST.keys(): 
        to_delete_unwatch.append(request.POST.getlist(i)[1])

    mls_ids_conv = ", ".join([str(x) for x in to_delete_unwatch])

    my_query = queries["delete_unwatch_row"] %mls_ids_conv

    cursor = db.cursor()
    cursor.execute(my_query)
    db.commit()
    cursor.close()

    return HttpResponse('whatevs')


def undelete(request):

    to_undelete = []
    for i in request.POST.keys(): 
        to_undelete.append(request.POST.getlist(i)[1])

    mls_ids_conv = ", ".join([str(x) for x in to_undelete])

    my_query = queries["undelete_row"] %mls_ids_conv
    
    cursor = db.cursor()
    cursor.execute(my_query)
    db.commit()
    cursor.close()


    return HttpResponse('whatevs')



def add_watch_list(request):
    to_add = []
    for i in request.POST.keys(): 
        to_add.append(request.POST.getlist(i)[1])

    mls_ids_conv = ", ".join([str(x) for x in to_add])

    my_query = queries["add_watch_list"] %mls_ids_conv
    
    cursor = db.cursor()
    cursor.execute(my_query)
    db.commit()
    cursor.close()


    return HttpResponse('whatevs')

def remove_watch_list(request):
    to_add = []
    for i in request.POST.keys(): 
        to_add.append(request.POST.getlist(i)[1])


    mls_ids_conv = ", ".join([str(x) for x in to_add])

    my_query = queries["remove_watch_list"] %mls_ids_conv
    
    cursor = db.cursor()
    cursor.execute(my_query)
    db.commit()
    cursor.close()


    return HttpResponse('whatevs')


def update_note(request):
 
    mls_id, note_input = request.POST["mls_id"], request.POST["note_input"]
    query = queries["update_note"] %(note_input, mls_id)
    
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()
    cursor.close()
    return HttpResponse('whatevs')


def get_main(request):
    query = queries["get_not_deleted_not_hotlist"]
    
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()

    return_data = result[:2]

    return render(request, 'mlsapp/data.html', {'mydata': return_data})


def watch_list(request):
    query = queries["get_watchlist"]

    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()

    if not result:
        result = [(),]

    return render(request, 'mlsapp/watch_list.html', {'mydata': result})


def deleted(request):
    query = queries["get_deleted"]

    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()

    if not result:
        result = [(),]

    return render(request, 'mlsapp/deleted.html', {'mydata': result})


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
