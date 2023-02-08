from django.db import models

# Create your models here.

GENDER = (
    ('M','male'),
    ('F','female'),
    ('o','Others')
)

CLASSLIST = (
    ('9','9'),
    ('10','10'),
    ('11','11'),
    ('12','12'),
    ('13','13'),
    ('14','14'),
    ('15','15'),
    ('16','16'),
)

class Classes(models.Model):
    className = models.CharField(max_length=200, choices=CLASSLIST)

    def __str__(self):
        return self.ClassName
    

class Student(models.Model):
    full_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
   
    gender = models.CharField(max_length=10,choices=GENDER)
    nationality = models.CharField(max_length=20, choices=(('Indian','Indian'),('Other','Other')))
    address = models.TextField()
    city = models.CharField(max_length=30, choices=(('Purnea','Purnea'),('Patna','Patna')))
    state = models.CharField(max_length=200)
    pincode = models.IntegerField()
    contact = models.CharField(max_length=15)
    image = models.ImageField(upload_to='students/',null=True, blank=True)
    dob = models.DateField()
    className = models.OneToOneField('Classes', on_delete=models.CASCADE)

