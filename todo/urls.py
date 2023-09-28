from django.urls import path
from . import views


urlpatterns = [
    path('', views.todo_list, name='todo'),
    path('<int:id>',views.todo_detail)
]

