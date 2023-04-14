from django.db import models


# Create your models here.

class Members(models.Model):
    name = models.CharField(max_length=40)
    host = models.CharField(max_length=255)
    #program_id = models.IntegerField
    #cores = models.IntegerField(default=1)
    cpu_usage = models.IntegerField()
    #status = models.CharField
    #memory_usage = models.FloatField
    #n_threads = models.IntegerField

    def __str__(self) -> str:
        return self.name

class all_users_data(models.Model):
    program_name = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    host = models.CharField(max_length=255)
    program_id = models.IntegerField()
    cores = models.IntegerField(default=1)
    cpu_usage = models.IntegerField()
    status = models.CharField(max_length=255)
    memory_usage = models.FloatField()

    def __str__(self) -> str:
        return self.name

