from django.db import models
from django.utils import timezone

# Create your models here.
class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """ Returns a string repersentation of a message."""
        date = timezone.localtime(self.log_date)

        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"
    

# Models for catalog items

# Categories and tags should be unique
# They definitely should not simply be random strings - the DB should define
#  what they are.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name