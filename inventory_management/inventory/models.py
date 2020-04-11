from django.db import models

# Create your models here.


class Device(models.Model):
    type = models.CharField(max_length=100, blank=False)
    price = models.IntegerField()

    choice = (
        ('Available', 'itme is available'),
        ('sold', 'item sold'),
        ('restock', 'item is restocking in few days')
    )
    status = models.CharField(max_length=100, choices=choice, default="Sold")
    issues = models.CharField(max_length=100, default="No Issue")

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type:{0} Price:{1}'.format(self.type, self.price)


class Laptop(Device):
    pass


class Desktop(Device):
    pass


class Mobile(Device):
    pass
