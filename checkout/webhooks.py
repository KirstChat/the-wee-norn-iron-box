from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

# from checkout.webhook_handler import Stripe_Handler

import stripe


@require_POST
@csrf_exempt
def webhook(request):
    # Setup
    webhook_secret = settings.STRIPE_WEBHOOK_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )
    except ValueError as e:
        # Invalid payload
        print(e)
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print(e)
        return HttpResponse(status=400)
    except Exception as e:
        print(e)
        return HttpResponse(content=e, status=400)

    print('Success!')
    return HttpResponse(status=200)
    
    # Handle the event
    # if event.type == 'payment_intent.succeeded':
    #     payment_intent = event.data.object # contains a stripe.PaymentIntent
    #     print('PaymentIntent was successful!')
    # elif event.type == 'payment_method.attached':
    #     payment_method = event.data.object # contains a stripe.PaymentMethod
    #     print('PaymentMethod was attached to a Customer!')
    # # ... handle other event types
    # else:
    #     print('Unhandled event type {}'.format(event.type))

    # return HttpResponse(status=200)
