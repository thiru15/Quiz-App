from django.contrib import admin
from django.urls import path
from testapp import views
from django.conf.urls import url
app_name = 'testapp'

urlpatterns = [
    path('',views.index,name="index"),
    url(r'^signup/$', views.register, name='register'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
        url(r'^user_login/$',views.user_login,name='user_login'),
    path('home/',views.home,name="home"),
    path('quiz1/',views.quiz1,name="quiz1"),
    path('quiz2/',views.quiz2,name="quiz2"),
    path('<int:user_id>/finish1/',views.finish1,name='finish1'),
    path('<int:user_id>/finish2/',views.finish2,name='finish2'),
    path('<int:user_id>/finish/',views.finish,name='finish'),
    #path('<int:pk>/results/',views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote1/', views.vote1, name='vote1'),
    path('<int:question_id>/vote2/',views.vote2,name='vote2'),
        #url(r'^<int:pk>/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^user_logout/$',views.user_logout,name='user_logout'),
]