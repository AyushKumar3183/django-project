from faker import Faker
import random
from .models import *

fake = Faker()

def seed_db(n=10) -> list:
    try:
        students=[]
        for i in range(n):
            department_obj = list(Department.objects.all())  # Convert to list
            
            # Check if the department_obj list is empty
            if not department_obj:
                print("No departments available.")
                return  # Exit the function if there are no departments
            
            random_index = random.randint(0, len(department_obj) - 1)
            department = department_obj[random_index]

            student_id = f"STU-{random.randint(100, 999)}" 
            student_name = fake.name()
            student_age = random.randint(20, 30)
            student_email = fake.email()    
            student_address = fake.address()
               

            student_id_obj = StudentId.objects.create(student_id=student_id)
            student_obj = Student.objects.create(
                department=department, 
                student_id=student_id_obj, 
                student_name=student_name,
                student_age=student_age,
                student_email=student_email,  
                student_address=student_address,   
            ) 
            students.append(student_obj)
        return students

    except Exception as e:
        print(e)



def ayush(n) -> None:
   

    new_students = seed_db(n)

    subjects = Subject.objects.all()  # Get all existing subjects

    for subject in subjects:
     for student in new_students:
        marks = random.randint(1, 100)  # Assign random marks
        SubjectMark.objects.create(
            student=student,
            subject=subject,
            marks=marks,
        )


