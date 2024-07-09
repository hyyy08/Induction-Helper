# Database Schema for DatabaseUser
# ./backend/core/models/databaseUser_model.py

from django.db import models

class DatabaseUser(models.Model):
    userID = models.IntegerField(primary_key=True) 
    email = models.CharField(max_length=254)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    userDate = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.firstName} {self.lastName} ({self.userID})"