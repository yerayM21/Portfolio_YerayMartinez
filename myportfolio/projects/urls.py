from . import views
from django.urls import path

urlpatterns = [
    path('', views.project_list,name='project_list'),
    path('add',views.add_project,name='add_project'),
]