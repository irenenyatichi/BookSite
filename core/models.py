from django.db import models

# Create your models here.
class Record(models.Model):
    book_Title = models.TextField (help_text='Enter book title'),
    author_Name = models.TextField (default="Enter the authors' name")

def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name