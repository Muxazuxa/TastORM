from rest_framework import generics, serializers, permissions
from .models import Task, TaskStatus
from .serializers import TaskSerializer, TaskStatusSerializer

# Create your views here.


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.AllowAny, )


class TaskDetailView(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permissions_classes = (permissions.AllowAny, )


class StatusListView(generics.ListAPIView):
    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusSerializer
    permissions_classes = (permissions.AllowAny,)


class StatusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusSerializer
    permissions_classes = (permissions.AllowAny, )


class FilterView(generics.ListAPIView):
    queryset = Task.objects.values_list('description', 'created')\
                            .filter(status__status=3)\
                            .filter(created__gte='2019-04-01 00:00:00', created__lte='2019-09-30 23:59:59')
    serializer_class = TaskSerializer
    permissions_classes = (permissions.AllowAny, )

    # SELECT "task_task"."description", "task_task"."created" FROM "task_task"
    # INNER JOIN "task_taskstatus" ON ("task_task"."id" = "task_taskstatus"."task_id")
    # WHERE ("task_taskstatus"."status" = 3
    # AND "task_task"."created" >= 2019-04-01 00:00:00 AND "task_task"."created" <= 2019-04-30 23:59:59)
