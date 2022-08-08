from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('canines/', views.canines_index, name='index'),
  path('canines/<int:canine_id>', views.canines_detail, name='detail'),
  path('canines/create/', views.CanineCreate.as_view(), name='canines_create'),
  path('canines/<int:pk>/update/', views.CanineUpdate.as_view(), name='canines_update'),
  path('canines/<int:pk>/delete/', views.CanineDelete.as_view(), name='canines_delete'),
]
