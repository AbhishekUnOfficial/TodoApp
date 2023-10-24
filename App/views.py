from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .models import TodoModel
from .forms import TodoForm


class TaskListView(ListView):
    model = TodoModel
    template_name = "App/all_task.html"
    context_object_name = "tasks"


class TaskDetailView(DetailView):
    model = TodoModel
    template_name = "App/task_detail.html"
    context_object_name = "task"


class TaskCreateView(CreateView):
    model = TodoModel
    form_class = TodoForm
    template_name = "App/create_task.html"
    success_url = reverse_lazy("all-task")


class TaskDeleteView(DeleteView):
    model = TodoModel
    context_object_name = "task"
    template_name = "App/delete_task.html"
    success_url = reverse_lazy("all-task")


class TaskUpdateView(UpdateView):
    model = TodoModel
    form_class = TodoForm
    context_object_name = "task"
    template_name = "App/update_task.html"
    success_url = reverse_lazy("all-task")
