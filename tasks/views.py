from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from tasks.models import Task, Tag
from .forms import TaskCreateForm, CompleteForm


class IndexView(ListView):
    template_name = 'todo/index.html'
    context_object_name = 'tasks'
    model = Task

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['CompleteForm'] = CompleteForm()
        return context


class TaskUpdateView(UpdateView):
    model = Task
    fields = ("__all__")
    success_url = reverse_lazy('index')
    template_name = 'todo/task-form.html'


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('index')
    template_name = 'todo/task-form.html'

    def form_valid(self, form):
        form.instance.assignee = self.request.user
        return super().form_valid(form)


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('index')
    template_name = 'todo/delete-task.html'


class SwitchTaskView(View):
    def post(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = Task.objects.get(id=task_id)
        task.is_done = not task.is_done
        task.save()
        return redirect('index')


class TagsListView(ListView):
    template_name = 'todo/tags-list.html'
    context_object_name = 'tags'
    model = Tag


class TagUpdateView(UpdateView):
    model = Tag
    fields = ("__all__")
    success_url = reverse_lazy('tags-list')
    template_name = 'todo/task-form.html'


class TagCreateView(CreateView):
    model = Tag
    fields = ("__all__")
    success_url = reverse_lazy('tags-list')
    template_name = 'todo/task-form.html'


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy('tags-list')
    template_name = 'todo/delete-task.html'
