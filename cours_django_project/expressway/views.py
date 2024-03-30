from django.shortcuts import render, redirect
from expressway.models import Trains
from expressway.forms import TrainsForm
import random

def index(request):
    allTrains = Trains.objects.all()

    return render(request, "expressway/index.html", {

        "trains": allTrains
    })

def show(request):
    return render(request, "expressway/show.html", {})

def show_id(request, id_train):
    myTrain = Trains.objects.get(trainID=id_train)
    allTrains = Trains.objects.all()

    max_id = allTrains.order_by('-trainID').first().trainID
    suivant = int(id_train) + 1 if int(id_train) < max_id else allTrains.order_by('trainID').first().trainID

    min_id = allTrains.order_by('trainID').first().trainID
    precedent = int(id_train) - 1 if int(id_train) > min_id else max_id

    return render(request, "expressway/show_id.html", {
        "type": myTrain.type,
        "n": myTrain.n,
        "destination": myTrain.destination,
        "heure": myTrain.heure,
        "voie": myTrain.voie,
        "precedent": precedent,
        "suivant": suivant,
    })


def aleatoir(request):

    allTrains = Trains.objects.all()
    random_train = random.choice(allTrains)
    return render(request, "expressway/aleatoir.html", {

        "type": random_train.type,
        "n": random_train.n,
        "destination": random_train.destination,
        "heure": random_train.heure,
        "voie": random_train.voie,
    })

def addTrain(request):
    if request.method == 'POST':
        form = TrainsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TrainsForm()
    return render(request, 'expressway/addTrain.html', {
        'form': form
    })
