from django.db import models

# Create your models here.
class CourseModel(models.Model):
    title = models.CharField(max_length=200)
    instructor = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title