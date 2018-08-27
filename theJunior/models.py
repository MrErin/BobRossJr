from django.db import models


class Birthday(models.Model):
    date = models.DateField(blank=True, null=True)
    name = models.CharField(default="", max_length=50)
    greeting = models.CharField(default="", max_length=50)

    class Meta:
        db_table = "Birthday"

    def __str__(self):
        return self.name
