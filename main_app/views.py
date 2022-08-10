from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Canine, Trick
from .forms import GroomingForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

  # Add new view
def canines_index(request):
    canines = Canine.objects.all()
    return render(request, 'canines/index.html', { 'canines': canines })

def canines_detail(request, canine_id):
    canine = Canine.objects.get(id=canine_id)
    id_list = canine.tricks.all().values_list('id')
    tricks_canine_doesnt_have = Trick.objects.exclude(id__in=id_list)
    grooming_form = GroomingForm()
    return render(request, 'canines/detail.html', { 'canine': canine, 'grooming_form': grooming_form, 'tricks': tricks_canine_doesnt_have })

def add_grooming(request, canine_id):
  form = GroomingForm(request.POST)
  if form.is_valid():
    new_grooming = form.save(commit=False)
    new_grooming.canine_id = canine_id
    new_grooming.save()
  return redirect('detail', canine_id=canine_id)

class CanineCreate(CreateView):
  model = Canine
  fields = ['name', 'breed', 'color', 'description', 'age']
  # success_url = '/cats/'

class CanineUpdate(UpdateView):
  model = Canine
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'color', 'description', 'age']

class CanineDelete(DeleteView):
  model = Canine
  success_url = '/canines/'

class TrickList(ListView):
  model = Trick

class TrickDetail(DetailView):
  model = Trick

class TrickCreate(CreateView):
  model = Trick
  fields = '__all__'

class TrickUpdate(UpdateView):
  model = Trick
  fields = ['name', 'difficulty']

class TrickDelete(DeleteView):
  model = Trick
  success_url = '/tricks/'

def assoc_trick(request, canine_id, trick_id):
  Canine.objects.get(id=canine_id).tricks.add(trick_id)
  return redirect('detail', canine_id=canine_id)

def disassoc_trick(request, canine_id, trick_id):
  Canine.objects.get(id=canine_id).tricks.remove(trick_id)
  return redirect('detail', canine_id=canine_id)