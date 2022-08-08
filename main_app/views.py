from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Canine

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
    return render(request, 'canines/detail.html', { 'canine': canine })

class CanineCreate(CreateView):
  model = Canine
  fields = '__all__'
  # success_url = '/cats/'

class CanineUpdate(UpdateView):
  model = Canine
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'color', 'description', 'age']

class CanineDelete(DeleteView):
  model = Canine
  success_url = '/canines/'