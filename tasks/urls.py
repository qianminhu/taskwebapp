from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = patterns('',
  url(r'^$', views.TaskList.as_view(), name='task_list'),
  url(r'^new$', views.TaskCreate.as_view(), name='task_new'),
  url(r'^edit/(?P<pk>\d+)$', views.TaskUpdate.as_view(), name='task_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.TaskDelete.as_view(), name='task_delete'),
)


urlpatterns += staticfiles_urlpatterns()