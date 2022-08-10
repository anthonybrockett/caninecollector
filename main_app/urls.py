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
  path('cats/<int:canine_id>/add_grooming/', views.add_grooming, name='add_grooming'),
  path('tricks/', views.TrickList.as_view(), name='tricks_index'),
  path('tricks/<int:pk>/', views.TrickDetail.as_view(), name='tricks_detail'),
  path('tricks/create/', views.TrickCreate.as_view(), name='tricks_create'),
  path('tricks/<int:pk>/update/', views.TrickUpdate.as_view(), name='tricks_update'),
  path('tricks/<int:pk>/delete/', views.TrickDelete.as_view(), name='tricks_delete'),
  path('canines/<int:canine_id>/assoc_trick/<int:trick_id>/', views.assoc_trick, name='assoc_trick'),
  path('canines/<int:canine_id>/disassoc_trick/<int:trick_id>/', views.disassoc_trick, name='disassoc_trick'),
]
