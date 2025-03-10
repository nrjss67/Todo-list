from django.urls import path
from . import views

urlpatterns = [
    path("tasks/", views.TaskListView.as_view(), name="task_list"),
    path("tasks/create/", views.TaskCreateView.as_view(), name="task_create"),
    path("tasks/update/<int:pk>/", views.TaskUpdateView.as_view(), name="task_update"),
    path("tasks/delete/<int:pk>/", views.TaskDeleteView.as_view(), name="task_delete"),
    path("tags/", views.TagListView.as_view(), name="tag_list"),
    path("tags/create/", views.TagCreateView.as_view(), name="tag_create"),
    path("tags/update/<int:pk>/", views.TagUpdateView.as_view(), name="tag_update"),
    path("tags/delete/<int:pk>/", views.TagDeleteView.as_view(), name="tag_delete"),
]
