from django.shortcuts import render
from django.views import generic
from django.contrib import messages

from restaurant.forms import OrderForm

from .models import Food, SuggestionCritics


class Home(generic.ListView):
    model = Food
    context_object_name = "foods"
    template_name = "home.html"


class Breakfast(Home):
    queryset = Food.objects.filter(food_types__title="صبحانه")


class Lunch(Home):
    queryset = Food.objects.filter(food_types__title="ناهار")


class Dinner(Home):
    queryset = Food.objects.filter(food_types__title="شام")


class FastFood(Home):
    queryset = Food.objects.filter(food_types__title="فست فود")


class Persian(Home):
    queryset = Food.objects.filter(food_types__title="ایرانی")


class Drink(Home):
    queryset = Food.objects.filter(food_types__title="نوشیدنی")


class Detail(generic.DetailView):
    model = Food
    # context_object_name = "food"
    template_name = "detail.html"


class AboutUs(generic.TemplateView):
    template_name = "about_us.html"


def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        text = request.POST.get("description")
        SuggestionCritics.objects.create(
            name=name,
            email=email,
            text=text,
        )
        context = {
            "name": name,
            "text": text,
        }
        return render(request, "contact_us_sent.html", context)
    return render(request, "contact_us.html")


class FoodOrder(generic.DetailView):
    model = Food
    template_name = "order.html"

    def post(self, request, *args, **kwargs):
        order_form = OrderForm(request.POST)
        context = {"food": self.get_object(), "form": order_form}
        if order_form.is_valid():
            phone_number = order_form.cleaned_data.get("phone_number")
            if not phone_number.isdigit():
                messages.error(request, "شماره تلفن را به درستی وارد کنید")
                return render(request, "order.html", context)
            order_form.save()
            context = {
                "name": order_form.cleaned_data.get("name"),
                "phone_number": phone_number,
                "amount": order_form.cleaned_data.get("amount"),
            }
            return render(request, "order_successful.html", context)
        messages.error(request, order_form.errors)
        return render(request, "order.html", context)
