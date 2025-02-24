from django.utils.timezone import now
import logging


logger = logging.getLogger('middleware')


class ResponseTimerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start_time = now()
        response = self.get_response(request)
        end_time = now()

        duration = end_time - start_time

        logger.info(f"Request to {request.path} took {duration} seconds")

        return response
