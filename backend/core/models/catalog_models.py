from django.db import models
from core.models import Category, Equipment

# ./backend/core/models/catalog_model.py

class Catalog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    equipmentName = models.ForeignKey(Equipment, on_delete=models.CASCADE)

    def __str__(self):
       return f"{self.category} - {self.equipmentName}" #return unstring error