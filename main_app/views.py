from django.shortcuts import render

from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Canine:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

canines = [
  Canine('Snow', 'Samoyed', 'Big White Fluffer', 4),
  Canine('Loki', 'Siberian Husky', 'Boundlessly Energetic', 0),
  Canine('Odin', 'Golden Retreiver', 'Man\'s Best Friend', 7)
]


# Create your views here.
def home(request):
  return HttpResponse('<h1>Welcome to the Home Page</h1>')

def about(request):
  return render(request, 'about.html')

  # Add new view
def canines_index(request):
  return render(request, 'canines/index.html', { 'canines': canines })
