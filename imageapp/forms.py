# from django.db import models  
# from django.forms import fields  
# from .models import UploadImage  
# from django import forms  
      
      
# class UserImageForm(forms.ModelForm):  
#     class meta:  
#         models = UploadImage  
#         fields = '__all__'  


from django import forms
from .models import Image, Product


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')

class ProductForm(forms.ModelForm):
    class Meta:
     model = Product
    fields = "__all__"

class OrderForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['order_status', 'items']

