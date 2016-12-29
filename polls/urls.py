from django.conf.urls import url
from polls import views
urlpatterns = [
    url(r'^$', views.poll_index,name='index'),
    url(r'^(?P<poll_id>\d+)/$', views.poll_detail, name='detail'),
    url(r'^(?P<poll_id>\d+)/result/$', views.poll_result, name='result'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.poll_vote, name='vote'),
    url(r'^add/$', views.poll_add, name='add'),
    url(r'^email/$', views.poll_email, name='email'),
    url(r'^makehtml/$', views.poll_makehtml, name='makehtml'),
    url(r'^login/$', views.poll_login, name='login'),
]