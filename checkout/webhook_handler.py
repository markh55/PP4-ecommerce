from django.http import HttpResponse
from checkout.models import Order
import stripe

class StripeWH_Handler:
    """Handle Stripe webhooks."""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event.
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe.
        """
        intent = event.data.object
        pid = intent.id
        # save info / order history
        save_info = intent.metadata.get('save_info')
        order_number = intent.metadata.get('order_number')

        if order_number:
            try:
                order = Order.objects.get(order_number=order_number)
                order.payment_status = 'Paid'
                order.save()
                if save_info == 'true' and order.user:
                    profile = order.user.profile
                    stripe_charge = stripe.Charge.retrieve(intent.latest_charge)
                    profile.default_phone_number = stripe_charge.billing_details.phone
                    profile.default_email = stripe_charge.billing_details.email
                    profile.save()
            except Order.DoesNotExist:
                pass

        return HttpResponse(
            content='Payment intent succeeded!',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe.
        """
        return HttpResponse(
            content='Payment intent failed.',
            status=200
        )
