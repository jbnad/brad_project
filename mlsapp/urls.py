from django.conf.urls import patterns, url

from mlsapp import views

urlpatterns = patterns('',
    url('^$', views.get_main, name='get_main'),
    #url('^get_main$', views.get_main, name='get_main'),
    url('^delete_rows$', views.delete_rows, name='delete_rows'),
    url('^update_note$', views.update_note, name='update_note'),
    url('^add_watch_list$', views.add_watch_list, name='add_watch_list'),
    url('^remove_watch_list$', views.remove_watch_list, name='remove_watch_list'),
    url('^un_watch_and_delete_and_rows$', views.un_watch_and_delete_and_rows, name='un_watch_and_delete_and_rows'),
    url('^watch_list$', views.watch_list, name="watch_list"),
    url('^deleted$', views.deleted, name="deleted"),
    url('^undelete_rows$', views.undelete, name="undelete"),
)
