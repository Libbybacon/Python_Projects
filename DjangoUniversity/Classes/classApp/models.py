from django.db import models


# Create object djangoClasses with attributes
class djangoClasses(models.Model):
    Title = models.CharField(max_length=30, default='')
    Course_Number = models.IntegerField(primary_key=True)
    Instructor_Name = models.CharField(max_length=50, default='')
    Duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.Title
