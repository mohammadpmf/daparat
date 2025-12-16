from django.dispatch import receiver, Signal
from django.contrib.auth.signals import user_logged_in
from .functions import send_email

pizza_ordered = Signal()


@receiver(user_logged_in)
def after_login(sender, request, user, **kwargs):
    send_email()


@receiver(pizza_ordered)
def announce_pizza(sender, **kwargs):
    print("Pizza order received 🚀")