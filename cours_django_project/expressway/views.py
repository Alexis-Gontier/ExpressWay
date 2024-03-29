from django.shortcuts import render, redirect
from expressway.models import Trains

def index(request):
    allTrains = Trains.objects.all()

    return render(request, "expressway/index.html", {

        "trains": allTrains
    })

def show(request):
    return render(request, "expressway/show.html", {})

def show_id(request, id_train) :
    myTrain = Trains.objects.get(trainID = id_train)

    return render(request, "expressway/show_id.html", {
        "type": myTrain.type,
        "n": myTrain.n,
        "destination": myTrain.destination,
        "heure": myTrain.heure,
        "voie": myTrain.voie,
        "precedent" : int(id_train) - 1,
        "suivant" : int(id_train) + 1,
    })


def random(request):
    return render(request, "expressway/random.html", {})

def addTrain(request):
    return render(request, "expressway/addTrain.html", {})