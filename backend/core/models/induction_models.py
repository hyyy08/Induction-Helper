# Database Schema for Induction models
# ./backend/base/models/induction_model.py

from django.db import models
from .databaseUser_models import DatabaseUser
from .equipment_models import Equipment
from .category_models import Category

class Induction(models.Model):
    userID = models.ForeignKey(DatabaseUser, on_delete=models.CASCADE)
    equipmentName = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    dateAdded = models.DateField(auto_now_add=True)
    dateCompleted = models.DateField(null=True, blank=True)
    completionStatus = models.BooleanField()
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['userID', 'equipmentName', 'category'], name='unique_induction')
        ]

    