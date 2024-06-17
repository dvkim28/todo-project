from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="tasks")
    deadline = models.DateTimeField(
        null=True, blank=True,
    )
    is_done = models.BooleanField(default=False)
    assignee = models.ForeignKey(AUTH_USER_MODEL,
                                 on_delete=models.CASCADE)
    descr = models.TextField(blank=True)

    class Meta:
        ordering = ['is_done', '-created_at']
