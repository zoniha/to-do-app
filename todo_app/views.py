from django.views import generic
from django.urls import reverse_lazy
from . import models


class TodoList(generic.ListView):
    template_name = 'list.html'
    model = models.TodoModel


class TodoDetail(generic.DeleteView):
    template_name = 'detail.html'
    model = models.TodoModel


class TodoCreate(generic.CreateView):
    template_name = 'create.html'
    model = models.TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')


class TodoDelete(generic.DeleteView):
    template_name = 'delete.html'
    model = models.TodoModel
    success_url = reverse_lazy('list')


class TodoUpdate(generic.UpdateView):
    template_name = 'update.html'
    model = models.TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')
