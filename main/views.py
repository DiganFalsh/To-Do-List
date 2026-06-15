from django.shortcuts import render, get_object_or_404, redirect

from .models import Task

# Create your views here.
def task_list(request):
    tasks = Task.objects.all().order_by("-created_at")
    active_tasks = tasks.filter(completed=False)
    return render(
        request, "tasks/index.html", {"tasks": tasks, "active_tasks": active_tasks}
    )

def task_add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        return redirect("task_list")
    return redirect("task_list")

def task_toggle(request, pk):
   task = get_object_or_404(Task, pk=pk)
   task.completed = not task.completed
   task.save()
   return redirect('task_list')

def task_delete(request, pk):
   task = get_object_or_404(Task, pk=pk)
   task.delete()
   return redirect('task_list')

def task_completed_delete(request):
   Task.objects.filter(completed=True).delete()
   return redirect('task_list')