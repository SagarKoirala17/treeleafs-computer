from django.db import models

# Create your models here.
class ComputerBrands(models.Model):
    brand_name=models.CharField(max_length=10)
    logo=models.ImageField(upload_to="photos/%Y/%m/%d/")

    def __str__(self):
        return self.brand_name

class ComputerSpecification(models.Model):
    generation=models.CharField(max_length=5)
    price_min=models.FloatField()
    price_max=models.FloatField()
    ram=models.IntegerField()
    brand=models.ForeignKey(ComputerBrands,on_delete=models.CASCADE)

    def __str__(self):
        return self.brand.brand_name
class Computer(models.Model):
    computer_code=models.CharField(max_length=5,unique=True)
    computer=models.ForeignKey(ComputerSpecification,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    unit_rate=models.PositiveIntegerField()
    total_price=models.PositiveIntegerField()

    def __str__(self):
        return self.computer_code



