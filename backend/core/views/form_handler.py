from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from core.models import DatabaseUser
import json

@require_http_methods(["POST"])
def create_user(request):
    # Parse the JSON data from the request body
    data = json.loads(request.body)
    
    # Create a new DatabaseUser instance
    user = DatabaseUser(
        email=data["email"],
        firstName=data["firstName"],
        lastName=data["lastName"],
    )
    user.save()
    
    # Return a success response
    return JsonResponse({"message": "User created successfully!", "userID": user.userID})
