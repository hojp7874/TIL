from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'), # NEW(GET), CREATE(POST) 합침
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'), # EDIT(GET), UPDATE(POST)
    path('<int:pk>/delete/', views.delete, name='delete'),
]