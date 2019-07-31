from django.db import models
from django.db.models.signals import post_save

# Create your models here.


class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=512)
    cost = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return self.description + "-" + str(self.cost)


class TaskStatus(models.Model):
    STATUS = (
        (0, 'Created'),
        (1, 'Taken'),
        (2, 'Reissued'),
        (3, 'On approve'),
        (4, 'Done'),
    )
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name='status')
    created = models.DateTimeField(auto_now_add=True)
    status = models.PositiveSmallIntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.task.description + ' ' + str(self.status)

    def create_status(sender, **kwargs):
        if kwargs['created']:
            task_status = TaskStatus.objects.create(task=kwargs['instance'])

    post_save.connect(create_status, sender=Task)