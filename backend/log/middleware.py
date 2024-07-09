import logging
from django.utils.timezone import now

logger = logging.getLogger(__name__)

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        self.process_request(request, response)
        return response

    def process_request(self, request, response):
        user = request.user if not request.user.is_anonymous else 'Anonymous'
        logger.info(f"{now()} - Request by {user}: {request.method} {request.path} - {response.status_code}")
        return response
