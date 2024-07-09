from rest_framework import serializers
from django.contrib.auth.models import User, Group
from django.core.validators import EmailValidator
from .models import DatabaseUser, Equipment, Category, Induction, Catalog

#serializer for admin user (instructor)
from django.contrib.auth.models import User
from rest_framework import serializers

class InstructorUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    email = serializers.EmailField(validators=[EmailValidator()])  # Validate email
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']

class InstructorUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    email = serializers.EmailField(validators=[EmailValidator()])  # Validate email
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    is_superuser = serializers.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'is_superuser']

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.core.validators import EmailValidator

class InstructorUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    email = serializers.EmailField(validators=[EmailValidator()])  # Validate email
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    is_superuser = serializers.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'is_superuser']

    def create(self, validated_data):
        # Set the username to be equal to the email address
        validated_data['username'] = validated_data['email']
        
        is_superuser = validated_data.pop('is_superuser', False)

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_staff=True,  # Default to staff member
            is_superuser=is_superuser
        )

        if not is_superuser:
            # Add user to the Instructor group if not a superuser
            group = Group.objects.get(name='Instructors')
            user.groups.add(group)
            user.save()

        return user



#Serializer for DatabaseUser
class DatabaseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = DatabaseUser
        fields = ['userID', 'email', 'firstName', 'lastName']
    
    def validate_userID(self, value):
        # Check if a user with the same userID already exists
        if DatabaseUser.objects.filter(userID=value).exists():
            raise serializers.ValidationError("Invalid: user already exists")
        return value
    
    def validate_email(self, value):
        # Email validation - email domain must be 'student.curtin.edu.au'
        if "@student.curtin.edu.au" not in value:
            raise serializers.ValidationError("Email domain must be student.curtin.edu.au")
        return value

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['equipmentName', 'equipmentDescription']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category', 'categoryDescription']

class CatalogSerializer(serializers.ModelSerializer):
    equipmentName = serializers.PrimaryKeyRelatedField(queryset=Equipment.objects.all(), write_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())       
    equipmentDetails = EquipmentSerializer(source='equipmentName', read_only=True)
    
    class Meta:
        model = Catalog
        fields = ['category', 'equipmentName', 'equipmentDetails']

class InductionSerializer(serializers.ModelSerializer):
    userID = serializers.PrimaryKeyRelatedField(queryset=DatabaseUser.objects.all(), write_only=True)
    equipmentName = serializers.PrimaryKeyRelatedField(queryset=Equipment.objects.all(), write_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())    
    
    userDetails = DatabaseUserSerializer(source='userID', read_only=True)
    equipmentDetails = EquipmentSerializer(source='equipmentName', read_only=True)
    
    class Meta:
        model = Induction
        fields = ['userID', 'userDetails', 'equipmentName', 'equipmentDetails', 'category', 'dateAdded', 'dateCompleted', 'completionStatus']
        
        
# Login Serialiser
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)
