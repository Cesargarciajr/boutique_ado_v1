from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)