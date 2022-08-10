from django.db import models
from django.urls import reverse

SERVICES = (
    ('B', 'Bath'),
    ('H', 'Haircut'),
    ('W', 'Walking')
)

# Create your models here.

class Trick(models.Model):
  name = models.CharField(max_length=50)
  difficulty = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('tricks_detail', kwargs={'pk': self.id})

class Canine(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    tricks = models.ManyToManyField(Trick)
    def __str__(self):
        return f'{self.name} {self.id}'
    def get_absolute_url(self):
        return reverse('detail', kwargs={'canine_id': self.id})

class Grooming(models.Model):
    date = models.DateField('grooming date')
    service = models.CharField(
        max_length=1,
        choices=SERVICES,
        default=SERVICES[0][0],
    )
    canine = models.ForeignKey(
        Canine, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_service_display()} on {self.date}"

    class Meta:
        ordering = ['-date']