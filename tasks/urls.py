
from django.contrib import admin
from django.urls import path

from .views import (IndexView,
                        TaskUpdateView,
                        TaskCreateView,
                        TaskDeleteView,
                        SwitchTaskView,
                        TagsListView,
                        TagUpdateView,
                        TagDeleteView,
                        TagCreateView)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('create-task/', TaskCreateView.as_view(), name='task-create'),
    path('task-switch/<int:pk>/',
         SwitchTaskView.as_view(), name='task-switch'),
    path('delete-task/<int:pk>/',
         TaskDeleteView.as_view(), name='task-delete'),
    path('tags/', TagsListView.as_view(), name='tags-list'),
    path('tag/<int:pk>/', TagUpdateView.as_view(), name='tag-update'),
    path('delete-tag/<int:pk>/', TagDeleteView.as_view(), name='tag-delete'),
    path('create-tag/', TagCreateView.as_view(), name='tag-create'),
]
