from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User=get_user_model()

class StudentManager(models.Manager):
    def get_queryset(self) :
        return super().get_queryset().filter(is_deleted=False)

class Recipe(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    recipe_name=models.CharField( max_length=100)
    recipe_description=models.TextField()
    recipe_image=models.ImageField(upload_to="recipe")

class Department(models.Model):
    department=models.CharField( max_length=100) 

    def __str__(self)->str: 
        return self.department 
    class Meta:
        ordering=['department'] 

class Subject(models.Model):
    subject_name=models.CharField(max_length=100)

    def __str__(self)->str: 
        return self.subject_name


class StudentId(models.Model):
    student_id=models.CharField( max_length=100)

    def __str__(self)->str: 
        return self.student_id

class Student(models.Model):
    department=models.ForeignKey(Department,related_name='depart',on_delete=models.CASCADE) 
    student_id= models.OneToOneField(StudentId, related_name='student', on_delete=models.CASCADE)
    student_name=models.CharField( max_length=100)
    student_age=models.IntegerField( default=18)
    student_email=models.EmailField( unique=True)    
    student_address=models.TextField( ) 
    is_deleted=models.BooleanField(default=False) 

    objects=StudentManager()
    admin_objects=models.Manager()  

    def __str__(self)->str:
        return self.student_name
    class Meta:
        ordering=['student_name'] 
        verbose_name="student"


class SubjectMark(models.Model):
    student=models.ForeignKey(Student, related_name="studentmark", on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,  on_delete=models.CASCADE) 
    marks= models.IntegerField()

    def __str__(self)->str:
        return f"{self.student.student_name}{self.subject.subject_name}"  
    
class Meta:
    Unique_together=['student','subject']    