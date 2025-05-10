from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Project(models.Model):
    """A project that groups multiple tasks under a user."""
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} (by {self.user.username})"

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["title"]


class Task(models.Model):
    """A task under a project, with status tracking and due date."""
    STATUS_CHOICES = (
        ("todo", "To Do"),
        ("doing", "Doing"),
        ("done", "Done"),
    )
    title = models.CharField(max_length=100)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="todo")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} [{self.status}]"

    def is_overdue(self):
        return self.due_date and self.due_date < timezone.now().date() and self.status != "done"

    class Meta:
        ordering = ["due_date"]
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
