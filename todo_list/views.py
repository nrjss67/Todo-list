from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from todo_list.forms import TaskCreateForm
from .models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo_list/task_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.order_by("-is_done").all()
        context["task_number"] = Task.objects.count()
        context["task_completed_number"] = Task.objects.filter(is_done=True).count()
        context["task_undone_number"] = Task.objects.filter(is_done=False).count()
        context["tags"] = Task.tags
        return context
    
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(id=request.POST.get("task_id"))
        
        if request.POST.get("is_done") == "true":
            task.is_done = True
        else:
            task.is_done = False
            
        task.save()
        return redirect("task_list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "todo_list/task_create.html"
    success_url = reverse_lazy("task_list")
    

class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "todo_list/task_update.html"
    fields = ["content", "deadline", "is_done", "tags"]
    success_url = reverse_lazy("task_list")
    
    
class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo_list/task_delete.html"
    success_url = reverse_lazy("task_list")
    

class TagListView(generic.ListView):
    model = Tag
    template_name = "todo_list/tag_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context
    
    
class TagCreateView(generic.CreateView):
    model = Tag
    template_name = "todo_list/tag_create.html"
    fields = ["name"]
    
    def get_success_url(self):
        referer = self.request.GET.get("next")
        if referer == "/create/":
            return reverse_lazy("task_create")
        print(referer)
        return reverse_lazy("tag_list")
    

class TagUpdateView(generic.UpdateView):
    model = Tag
    template_name = "todo_list/tag_update.html"
    fields = ["name"]
    success_url = reverse_lazy("tag_list")
    
    
class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo_list/tag_delete.html"
    success_url = reverse_lazy("tag_list")
