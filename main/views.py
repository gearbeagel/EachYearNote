from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from main.models import YearlyCards


# Create your views here.
def home(request):
    cards = YearlyCards.objects.all().order_by('-year')
    messages.info(request, 'Hey there, love. Have a look around. <3')
    return render(request, 'home.html', {'cards': cards})

def card_detail(request, slug):
    card = get_object_or_404(YearlyCards, slug=slug)
    return render(request, 'card_detail.html', {'card': card})