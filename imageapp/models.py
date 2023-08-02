
# # Create your models here.


# from django.db import models  
      
# class UploadImage(models.Model):  
#     name = models.CharField(max_length=200)  
#     image = models.ImageField(upload_to='images')  
      
#     def __str__(self):  
#         return self.caption  



from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=50)
    description = models.TextField(default='Its too yummy')
    image = models.ImageField(upload_to='images')
    order_status = models.BooleanField(default=False)
    items = models.IntegerField(default=0)

    def __str__(self):
        return self.name