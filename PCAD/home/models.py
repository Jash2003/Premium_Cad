from django.db import models
# Create your models here.
class Blog(models.Model):
    title = models.TextField()
    readtime = models.IntegerField(default=2)
    date = models.DateField()
    coverimage = models.ImageField(upload_to="blog_covers")
    content = models.TextField()

def __str__(self):
        return self.title

class Applicant(models.Model):
      jobrole = models.TextField()
      name = models.TextField()
      email = models.TextField()
      phone = models.TextField()
      location = models.TextField()
      exprience = models.TextField()
      resume = models.FileField(upload_to="resumes")


      


