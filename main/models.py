from django.db import models



class Customer(models.Model):
    name = models.CharField(max_length=55)
    paid = models.BooleanField(default=False)
    summa = models.PositiveIntegerField('berishi kerak bolgan sum ', default=0)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return "%s"%self.name


class Payment(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customers')
    month = models.CharField(max_length=55)
    summa = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "%s"%self.summa
