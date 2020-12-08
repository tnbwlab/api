from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        ordering = ['id']

class Product(models.Model):
    owner_id = models.ForeignKey(Owner, related_name='owners',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return '%s: %d' % (self.name, self.quantity)

    class Meta:
        ordering = ['name']