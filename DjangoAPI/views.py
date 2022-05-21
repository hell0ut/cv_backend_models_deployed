from rest_framework import viewsets
from .serializers import ImageSerializer
from .apps import DjangoapiConfig
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Image
from rest_framework.views import APIView
from rest_framework.response import Response
import torch
from rest_framework.decorators import action
from rest_framework.response import Response
import io
from PIL import Image as pil_img
from django.views.generic.edit import FormView
from .forms import FileFieldForm
import torchvision.transforms as transforms


model = DjangoapiConfig.cats_vs_dogs_model

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    @action(detail=False, methods=['post'])
    def predict(self,request):
        img_binary = request.FILES['image'].read()
        print('here')
        img = pil_img.open(io.BytesIO(img_binary))
        transfomer = transforms.Compose([transforms.Resize(255),
                                transforms.CenterCrop(224),
                                transforms.ToTensor()
                    ])
        img = transfomer(img)
        img = torch.reshape(img,(1,3,224,224))
        prediction = model(img)
        class_str = ''
        if prediction[0][1]>prediction[0,0]:
            class_str = 'dog'
        else:
            class_str = 'cat'
        return Response({'prediction': class_str})
