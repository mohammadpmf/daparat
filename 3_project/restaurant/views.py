from django.shortcuts import render, HttpResponse


def show_restaurant(request):
    context = {
        "name": "Mohammad",
        "age": 34,
        "favorite_colors": ["green", "blue", "cyan"],
        "father": {"name": "Ali", "surname": "Fallah"},
        "alaki": 19.5,
        "has_driving_license": True
    }
    return render(request, "index.html", context)


def show_drinks(request):
    context = {
        "images": [
            "imgs/ghahverh/6.jpg",
            "imgs/kebab/3.jpg",
            "imgs/kebab/4.jpg",
            "imgs/macaroni/3.jpg",
            "imgs/omlet/3.jpg",
            "imgs/pizza/2.jpg",
        ]
    }
    return render(request, "drinks.html", context)


def show_fast_food(request):
    return render(request, "fast_food.html")


def show_lunch(request):
    return render(request, "lunch.html")


def show_about_us(request):
    return render(request, "about_us.html")


def show_breakfast(request):
    return render(request, "breakfast.html")


def show_contact_us_sent(request):
    return render(request, "contact_us_sent.html")


def show_contact_us(request):
    return render(request, "contact_us.html")


def show_detail(request):
    return render(request, "detail.html")


def show_dinner(request):
    return render(request, "dinner.html")


def show_order_successful(request):
    return render(request, "order_successful.html")


def show_order(request):
    return render(request, "order.html")


def show_persian(request):
    return render(request, "persian.html")
