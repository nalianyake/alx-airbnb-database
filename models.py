from django.db import models

class Seed(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  user_id (Primary Key, UUID, Indexed)
  name  = models.CharField(max_length=255)
  email  = models.CharField(max_length=255)
  age  = models.VarField(max_length=255)