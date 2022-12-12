from django.urls import path
from .views import taskList, taskDetail, taskCreate, taskDelete, taskUpdate

urlpatterns = [
    path('', taskList.as_view(), name='tasks'),
    
]