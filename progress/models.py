from django.db import models

from home.models import UserProfile
from course.models import Lecture


class Progress(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, unique=False, related_name='progress')
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, unique=False, related_name='progress')
    completion = models.IntegerField(choices=((1, 'True'), (2, "False")), default=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [('lecture', 'student')]

