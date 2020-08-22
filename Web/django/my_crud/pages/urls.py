from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    # C
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    # R
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    # U
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
    # D
    path('<int:pk>/delete/', views.delete, name='delete'),
]
