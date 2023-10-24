from django.urls import path
from . import views


urlpatterns = [
    path("", views.TaskListView.as_view(), name="all-task"),
    path("create/", views.TaskCreateView.as_view(), name="create-task"),
    path("update/<slug:slug>/", views.TaskUpdateView.as_view(), name="update-task"),
    path("delete/<slug:slug>/", views.TaskDeleteView.as_view(), name="delete-task"),
    path("<slug:slug>/", views.TaskDetailView.as_view(), name="task-details"),
]
