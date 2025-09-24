from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name

class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='cars/', null=True, blank=True)
    vin = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"