from django.db import models

class BabyName(models.Model):
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=1)
    year = models.IntegerField()
    count = models.IntegerField()
    year_rank = models.IntegerField()

    class Meta:
        db_table = 'baby_names'  # This tells Django to use the existing 'baby_names' table

    def __str__(self):
        return f"{self.name} ({self.sex}, {self.year})"
