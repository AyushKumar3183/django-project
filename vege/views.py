from django.shortcuts import render, redirect
from .models import *  # Import your Recipe model
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model

User=get_user_model()

@login_required(login_url='/login/')
def recipe(request):
    if request.method == "POST":
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        Recipe.objects.create(
            recipe_image=recipe_image,
            recipe_name=recipe_name,
            recipe_description=recipe_description
        )

        return redirect('/recipe/')
    
    queryset = Recipe.objects.all()
    context = {'recipe': queryset}
    return render(request, "recipe.html", context)  # Ensure 'recipe.html' is in the right template directory

def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    context = {'recipe': queryset}
    return render(request, "update_recipe.html", context)

def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipe/')

def login_page(request):
    if request.method == "POST":
        phone_number = request.POST.get("phonenumber")
        password = request.POST.get("password")
        user = authenticate(request, phone_number=phone_number, password=password)

        if user is None:
            messages.error(request, 'Invalid phonenumber or password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/recipe/')

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone_number = request.POST.get("phonenumber")
        password = request.POST.get("password")
        
        if User.objects.filter(phone_number=phone_number).exists():
            messages.info(request, 'phonenumber already exists')
            return redirect('/register/')
        
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number
        )
        user.set_password(password)
        user.save()
        messages.success(request, 'You have created an account successfully')
        return redirect('/login/')  # Redirect to login after successful registration

    return render(request, 'register.html')  # Ensure this is outside the if block
from django.db.models import Q,Sum
def get_student(request):
    queryset=Student.objects.all()
    if request.GET.get('search'):
        search=request.GET.get('search')
        queryset=queryset.filter(
            Q(student_name__icontains=search)|
            Q(department__department__icontains=search)|
            Q(student_id__student_id__icontains=search)|
            Q(student_email__icontains=search) 
            )
 
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)  
    return render(request, 'student.html',{'page_obj':page_obj})

def See_Mark(request, student_id):

    queryset = SubjectMark.objects.filter(student__student_id__student_id=student_id)
    total_mark=queryset.aggregate(total_marks=Sum('marks'))
    ranks= Student.objects.annotate(marks=Sum("studentmark__marks")).order_by("marks")
    current_rank=-1
    i=1
    for rank in ranks :
        if student_id==rank.student_id.student_id:
            current_rank=i
            break
        i=i+1
            
    return render(request, 'mark.html', {'queryset': queryset,'total_mark':total_mark,'current_rank':current_rank})
