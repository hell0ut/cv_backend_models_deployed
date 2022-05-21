from django.apps import AppConfig
import os.path
from django.conf import settings
import torch


class DjangoapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DjangoAPI'
    MODEL_FILE = os.path.join(settings.MODELS,'dogs_vs_cats_vgg.pt')
    cats_vs_dogs_model = torch.load(MODEL_FILE,map_location=torch.device('cpu'))


