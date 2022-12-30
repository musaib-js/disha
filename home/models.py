from sre_parse import CATEGORIES
from tkinter import Text
from django.db import models

Category_Choices = (
    ('Engineering', 'Engineering'),
    ('Medical', 'Medical'),
    ('Nursing', 'Nursing'),
    ('All', 'All'),
)

class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 80)
    email = models.EmailField(max_length = 80)
    phone = models.IntegerField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return "Message From " +  self.name

class Email(models.Model):
    email = models.EmailField(max_length = 90)

    def __str__(self):
        return "Mail Request From " +  self.email

class Video(models.Model):
    sno = models.AutoField(primary_key = True)
    subject = models.CharField(max_length = 200)
    thumnbail = models.ImageField(upload_to = "media")
    video = models.FileField(upload_to = "media")
    speaker = models.CharField(max_length = 100)
    timeStamp = models.DateTimeField()
    desc = models.TextField()
    slug = models.CharField(max_length = 200)

    def __str__(self):
        return "Video By " + self.speaker

class Service(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 200)
    slugtwo = models.CharField(max_length = 150, default = "")
    subtitle= models.CharField(max_length = 250)
    image = models.ImageField(upload_to = "media", default = "")
    desc = models.TextField(default = "")
    video = models.FileField(upload_to= 'media', default = "")

    def __str__(self):
        return self.name

class College(models.Model):
    name = models.CharField(max_length = 350)
    location = models.CharField(max_length = 500)
    category = models.CharField(max_length=50, choices=Category_Choices, default = "All")
    photo = models.ImageField(upload_to="media")
    description = models.TextField()
    courses_offered = models.TextField()

    def __str__(self):
        return self.name

class Courses(models.Model):
    name = models.CharField(max_length = 350)
    category = models.CharField(max_length=50, choices=Category_Choices, default = "All")
    photo = models.ImageField(upload_to="media")
    description = models.TextField()
    offered_by = models.TextField()

    def __str__(self):
        return self.name
    

    


    


 


