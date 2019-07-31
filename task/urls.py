from django.urls import path
from .views import TaskListCreateView, TaskDetailView, StatusDetailView, StatusListView, FilterView

app_name = 'task'

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='task_list'),
    path('<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('status', StatusListView.as_view(), name='status_list'),
    path('<int:pk>/status', StatusDetailView.as_view(), name='status_detail'),
    path('filter', FilterView.as_view(), name='filter'),
]