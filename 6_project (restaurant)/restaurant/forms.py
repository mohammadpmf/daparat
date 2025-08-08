from django.forms import ModelForm

from restaurant.models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["name", "email" ,"phone_number", "amount"]