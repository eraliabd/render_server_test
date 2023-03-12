from django.db import models


class DollarCourse(models.Model):
    dollar_course = models.PositiveBigIntegerField()
    soum = models.PositiveBigIntegerField()
    dollar = models.PositiveBigIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dollar_course
