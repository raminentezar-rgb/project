from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=[
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('villa', 'Villa'),
    ])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='property_images/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class VisitRequest(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='visit_requests')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    preferred_date = models.DateField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.property.title}"

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_gallery/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.property.title}"
