from django.urls import path

from . import views


app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('author/', views.author, name='author'),
    path('quote/', views.quote, name='quote'),
    path('author-info/<str:name>/', views.author_info, name='author_info'),
    path('tag/<str:tag>/', views.found_by_teg, name='found_by_teg'),

]