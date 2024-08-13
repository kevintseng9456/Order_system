from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm
# from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# rooms = [
#     {'id':1, 'name':'Lets learn python!'},
#     {'id':2, 'name':'Design with me'},
#     {'id':3, 'name':'Frontend develope'},
# ]

# @csrf_exempt
def home(request):
    rooms = Room.objects.all()

    topics = Topic.objects.all()

    context = {'rooms': rooms, 'topics': topics}
    return render(request, 'app/home.html', context)

# @csrf_exempt
def room(request, pk):
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    room = Room.objects.all().get(id=pk)
    context = {'room': room}
    return render(request, 'app/room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        # print(request.POST)
    context = {'form': form}
    return render(request, 'app/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form': form}
    return render(request, "app/room_form.html", context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'app/delete.html', {'obj': room})