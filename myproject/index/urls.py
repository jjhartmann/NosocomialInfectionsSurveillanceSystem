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
    url(r'^database_search/$', views.database_search, name='database_search'),
    url(r'^blast/$', views.blast, name='blast'),
    url(r'^phylip_intro/$', views.phylip_intro, name='phylip_intro'),
    url(r'^symptoms/$', views.symptoms, name='symptoms'),
    url(r'^cause/$', views.cause, name='cause'),
    url(r'^about/$', views.about, name='about'),
    url(r'^tutorial/$', views.tutorial, name='tutorial'),
    url(r'^website_intro/$', views.website_intro, name='website_intro'),
    url(r'^project/$', views.project_intro, name='project_intro'),
]

