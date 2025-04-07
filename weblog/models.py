from django.db import models

# Create your models here.

class Post(models.Model):
    CHOICE_STATUS = [
        ('Published','Published'),
        ('Draft','Draft')
    ]
    title = models.CharField(max_length=150)
    description = models.TextField()
    status = models.CharField(max_length=50,choices=CHOICE_STATUS,default='Published')
    slug = models.SlugField(unique=True)
    avatar = models.ImageField(upload_to='',blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.username