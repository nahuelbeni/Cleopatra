from django.db import models
# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(default='noemail@example.com')
    phone = models.CharField(max_length=255,default='No phone number')
    country = models.CharField(max_length= 255, default='')

    def __str__(self):
        return str(self.name)    

class Course(models.Model):
    course_name = models.CharField(max_length= 255)
    day = models.IntegerField()
    # teacher =  models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    details = models.TextField(blank=True, default='')
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return str(self.course_name)
        
class Dancer(models.Model):
    dancerID = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length= 255)
    email = models.EmailField(default='noemail@example.com')
    country = models.CharField(max_length= 255)
    # courses = models.ForeignKey(Course, related_name='courses', on_delete=models.CASCADE, null=True)
    courses = models.ManyToManyField(Course, related_name='courses')
    

    def __str__(self):
        return str(self.name) 
    


