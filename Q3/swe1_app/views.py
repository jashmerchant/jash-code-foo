from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from .models import Poll

# Create your views here.


def index(request):
    poll = Poll.objects.get(id=1)
    if request.method == "POST":
        selected_option = request.POST["poll"]
        if selected_option == "option1":
            poll.option_one_count += 1
        elif selected_option == "option2":
            poll.option_two_count += 1
        elif selected_option == "option3":
            poll.option_three_count += 1
        else:
            return HttpResponse(400, "Invalid form")

        poll.save()

        return HttpResponseRedirect(reverse("swe1_app:results"))
    return render(request, "swe1_app/index.html", {"poll": poll})


def results(request):
    poll = Poll.objects.get(id=1)
    return render(request, "swe1_app/results.html", {"poll": poll})
