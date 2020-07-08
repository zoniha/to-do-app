from django.db import models

PRIORITY = (('danger', 'high'), ('primary', 'normal'), ('info', 'low'))


class TodoModel(models.Model):
    title = models.CharField(max_length=30)
    memo = models.TextField(blank=True)
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY,
    )
    duedate = models.DateField()

    def __str__(self):
        return self.title

