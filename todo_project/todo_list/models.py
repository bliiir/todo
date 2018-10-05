from django.db import models
from django.utils import timezone

class TodoList(models.Model):
    title =         models.CharField(max_length=50)
    completed =     models.IntegerField(default=0)

    def __str__(self):
        return self.title

class TodoItem(models.Model):
    todolist =      models.ForeignKey(TodoList, on_delete=models.CASCADE)
    name =          models.CharField(max_length=50)
    Description =   models.CharField(max_length=200)
    date_created =  models.DateTimeField('date created')
    due_date =      models.DateTimeField('date due')

    def __str__(self):
        return self.name

    def days_left(self):
        return self.due_date() - timeszone.now()
