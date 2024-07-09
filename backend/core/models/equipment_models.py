from django.db import models

# Database Schema for DatabaseUser
# ./backend/core/models/equipment_model.py

class Equipment(models.Model):
    equipmentName = models.CharField(primary_key=True, max_length=100)
    equipmentDescription = models.TextField(blank=True, default='')
    
    def __str__(self):
        return f"{self.equipmentName})"