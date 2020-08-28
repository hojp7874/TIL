from django.urls import path
from . import views

# 'articles/index/'
app_name = 'pages'
urlpatterns = [
    # pages/index/'
    path('index/', views.index, name='index')
]
