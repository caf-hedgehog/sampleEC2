"""
Definition of models.
"""

from django.db import models

# Create your models here.
class users(models.Model):
    class Meta:
        db_table = "users"

    id = models.AutoField(primary_key=True)  # é©ìÆçÃî‘
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
