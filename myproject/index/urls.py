__author__ = 'Jeremy'


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.indexview, name='index'),  # main index page.
    # url(r'^about/'), # about page.
    # url(r'^features/'), # features page.
    url(r'^login/$', views.loginview, name='login'),  #login page
    url(r'^logout/$', views.doctor_logout, name='logout'),  #logout page
    url(r'^login/verify/$', views.doctor_login, name='verifycredentials'),  # verify user
    #added by palmer,
    url(r'^register/$', views.doctor_register, name='register'),
    url(r'^register_success/$', views.doctor_register_success, name='register_success'),
    url(r'^data_graph/$', views.data_graph_json, name='data_graph_json'),
    url(r'^project/$', views.project_des, name='project_des'),
    url(r'^blast/$', views.blast, name='blast'),
    url(r'^phylib_intro/$', views.phylib_intro, name='phylib_intro'),
    url(r'^symptoms/$', views.symptoms, name='symptoms'),
    url(r'^cause/$', views.cause, name='cause'),
]

