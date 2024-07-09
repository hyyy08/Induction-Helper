from django.db import models

# ./backend/core/models/category_model.py

class Category(models.Model):
    category = models.CharField(max_length=20, primary_key=True)
    categoryDescription = models.TextField(blank=True, default='')
    
    def __str__(self):
        return self.category