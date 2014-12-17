from django.conf.urls import patterns, url, include

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<question_id>\d+)/vote2/$', views.vote2, name='vote2'),
    url(r'^(?P<question_id>\d+)/edit_q/$', views.edit_q, name='edit_q'),
    url(r'^(?P<question_id>\d+)/edit_a/$', views.edit_a, name='edit_a'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^add_question/$', views.add_question, name='add_question'), # NEW MAPPING!
    url(r'^add_choice/$', views.add_choice, name='add_choice'),
    url(r'^add_photo/$', views.photo_upload, name='add_photo'),
    url(r'^edit/$', views.EditView.as_view(), name='edit'),
    url(r'^older/$', views.OldView.as_view(), name='older'),
    url(r'^tag/$', views.tagView, name='tag'),
)