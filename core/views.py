from django.shortcuts import render
from core.models import Record
from django.shortcuts import reverse
from .forms import BookRegistrationForm
from utils import MongodbClient

def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
