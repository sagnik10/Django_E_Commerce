from django.db import models

class Product(models.Model):
    category=models.CharField(max_length=50)
    name= models.CharField(max_length=200)
    price = models.IntegerField()
    desciption = models.CharField(max_length=500)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.category

class Laptops(models.Model):
    category=models.CharField(max_length=50)
    name= models.CharField(max_length=200)
    price = models.IntegerField()
    desciption = models.CharField(max_length=500)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.category

class Mens(models.Model):
    category=models.CharField(max_length=50)
    name= models.CharField(max_length=200)
    price = models.IntegerField()
    desciption = models.CharField(max_length=500)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.category

class Womens(models.Model):
    category=models.CharField(max_length=50)
    name= models.CharField(max_length=200)
    price = models.IntegerField()
    desciption = models.CharField(max_length=500)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.category

class Furnitures(models.Model):
    category=models.CharField(max_length=50)
    name= models.CharField(max_length=200)
    price = models.IntegerField()
    desciption = models.CharField(max_length=500)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.category