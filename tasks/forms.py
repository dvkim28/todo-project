from django import forms

from tasks.models import Task


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'descr', 'tags']


class CompleteForm(forms.Form):
    task_id = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
