from django.db import models

GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
    ]

COUNTRY=[
    ('India','India'),
    ('Canada','Canada'),
    ('USA','USA'),
    ('China','China'),
]

CARD=[
    ('Cradit','Cradit'),
    ('Mail','Mail'),
    ('Perschool','Perschool'),
]


COURSE=[
    ('Language','Language'),
    ('Communication','Communication'),
    ('Business','Business'),
    ('Software','Software'),
    ('Social Media','Social Media'),
    ('Photography','Photography'),
    ('Web Designing','Web Designing'),
]

# Create your models here.
class Registration(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Password=models.CharField(max_length=25)
    CPassword=models.CharField(max_length=25)
    TNC=models.BooleanField(default=False,blank=True)

    def __str__(self):
        return self.Email
    

class Subscribe(models.Model):
    Email=models.EmailField(unique=True)

    def __str__(self):
        return self.Email
    

class Admission(models.Model):
    FstName=models.CharField(max_length=20)
    MidName=models.CharField(max_length=20)
    LstName=models.CharField(max_length=20)
    Dob=models.DateField()
    Gender=models.CharField(max_length=20,choices=GENDER)
    Country=models.CharField(max_length=30,choices=COUNTRY)
    Phone=models.PositiveIntegerField()
    Email=models.ForeignKey(Registration,on_delete=models.CASCADE)
    Address=models.CharField(max_length=100)
    Line=models.TextField(max_length=100)
    City=models.CharField(max_length=20)
    State=models.CharField(max_length=20)
    Code=models.PositiveIntegerField()
    Course=models.CharField(max_length=15,choices=COURSE)
    AdharCard=models.ImageField(upload_to='images/')
    Passport=models.ImageField(upload_to='images/')
    Fmarksheet=models.ImageField(upload_to='images/')
    Smarksheet=models.ImageField(upload_to='images/')
    Signature=models.ImageField(upload_to='images/')
    Payment=models.CharField(max_length=30,choices=CARD)
    Approved=models.CharField(max_length=20,default='pending')

    def __str__(self):
        return self.FstName
    


class Contact(models.Model):
    FstName=models.CharField(max_length=20)
    LstName=models.CharField(max_length=20)
    Subject=models.CharField(max_length=100)
    Email=models.EmailField()
    Message=models.CharField(max_length=150)

    def __str__(self):
        return self.Email

class Comment(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.ForeignKey(Registration,on_delete=models.CASCADE)
    Comment=models.CharField(max_length=200)
    
    def __str__(self):
        return self.Email
    

class Fqu(models.Model):
    Que=models.CharField(max_length=100)
    Ans=models.CharField(max_length=2000)

    def __str__(self):
        return self.Que

class Specific_Crc(models.Model):
    title=models.CharField(max_length=100)   

    def __str__(self):
        return self.title
     

class Cources(models.Model):
    cat=models.ForeignKey(Specific_Crc,on_delete=models.CASCADE)
    Book_lang = models.CharField(max_length=50)
    Book_price = models.PositiveIntegerField()
    Book_desc = models.CharField(max_length=1000)
    Book_img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.Book_lang
    

class Cart(models.Model):
    Email=models.ForeignKey(Registration,on_delete=models.CASCADE)
    Books=models.ForeignKey(Cources,on_delete=models.CASCADE)
    Quantity=models.PositiveIntegerField()
    Price=models.FloatField()
