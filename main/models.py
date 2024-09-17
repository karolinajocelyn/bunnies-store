from django.db import models
import uuid

# Create your models here.
class Product(models.Model):
    # Use a UUID as the primary key for this model
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Represents the name of the artist
    artist_name = models.CharField(max_length=100)
    
    # Represents the name of the album
    album_title = models.CharField(max_length=100)
    
    # Represents the price of the album
    price = models.IntegerField()
    
    # Represents the description of the album
    description = models.TextField()
    
    # This string method defines how the object is represented in the admin panel and elsewhere
    def __str__(self):
        return self.album_title