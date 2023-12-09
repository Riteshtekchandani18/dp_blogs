from django.urls import path
from . import views

urlspatterns =[
    path('', views.home_view, name='home'),
    path('add/', views.add_views, name='add'),
    path('myarticles/', views.my_articles, name='my_aricles'),
    path('article/<int:id>/likes', views.inc_like, name= 'inc_like'),
    path('article/<int:id>/details', views.detail_view, name='details'),
    path('article/<int:id>/delete',views.delete_view, name='delete'),
    path('aticles/<int:id>/edit' , views.edit_view, name='edit'),
]