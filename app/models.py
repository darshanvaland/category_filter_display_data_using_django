from django.db import models

# Create your models here.

class Register(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    contact=models.PositiveIntegerField()
    password=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class task(models.Model):
    user=models.ForeignKey(Register,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    decription=models.TextField()
    x=(
        (None, 'select category'),
        ('outdoor','outdoor'),
        ('indoor','indor')
    )
    category=models.CharField(max_length=12,choices=x,default=None)
    Create_date=models.DateTimeField()
    Complete_date=models.DateTimeField(auto_created=True,auto_now=True)

    def __str__(self):
        return self.name