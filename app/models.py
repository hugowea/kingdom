from django.db import models


class Kingdom(models.Model):
    kingdom_name = models.CharField(max_length=128)

    def __str__(self):
        return self.kingdom_name

class Subordinate(models.Model):
    name = models.CharField(max_length=128)
    kingdom = models.ForeignKey(to=Kingdom, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField()
    email = models.CharField(max_length=128)

    def __str__(self):
        return "name: " + self.name + " | kingdom: " + self.kingdom 

class King(models.Model):
    name = models.CharField(max_length=128)
    kingdom = models.ForeignKey(to=Kingdom, on_delete=models.CASCADE)

    def __str__(self):
        return "name: " + self.name + " | kingdom: " + self.kingdom 

class Test(models.Model):
    unique_code = models.ForeignKey(to=Kingdom, on_delete=models.CASCADE)