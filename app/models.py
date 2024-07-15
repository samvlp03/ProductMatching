from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models import Max

class Product(models.Model): #change the table name(if you want, otherwise in evry file let it be same.)
    category = models.CharField(max_length=255)
    model_no = models.CharField(max_length=255)
    part_no = models.CharField(max_length=255)
    serial_no = models.CharField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.serial_no:  # Only generate if serial_no is not set
            sequence_number = Product.objects.filter(model_no=self.model_no, part_no=self.part_no).count() + 1
            self.serial_no = f"{self.model_no}{self.part_no}{sequence_number:03}"
        super(Product, self).save(*args, **kwargs)
        
        #Enter your table name

    def __str__(self):
        return self.serial_no

class ScannedProduct1(models.Model):
    model_no = models.CharField(max_length=255)
    serial_no = models.CharField(max_length=255)
    part_no = models.CharField(max_length=255)
    scanned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.model_no}-{self.serial_no} - {self.part_no}"
