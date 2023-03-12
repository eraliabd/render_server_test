from django.db import models


class DollarCourse(models.Model):
    dollar_course = models.CharField(max_length=255)
    som_input = models.CharField(max_length=255, null=True, blank=True)
    dollar_input = models.CharField(max_length=255, null=True, blank=True)
    som = models.CharField(max_length=255)
    dollar = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dollar_course
