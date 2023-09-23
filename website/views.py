from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecord
from .models import Book
# Create your views here.


def home(request):
    books = Book.objects.all()
    students= Student.objects.all()



    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('website:home')
        else:
            messages.success(request, "Incorrect username or password")
            return redirect('website:home')
    else:
        return render(request, 'website/home.html', {'title':'Home Page', 'books':books,'students':students})




# def login(request):
#     return render(request,'webiste/login.html',{})





def user_logout(request):
    logout(request)
    messages.success(request,'You Have Been Logged Out!...')
    return redirect('website:home')





def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,'You Have Been Successfuly Registered ')
            return redirect('website:home')
    else:
        form = SignUpForm()

        return render(request,'website/register.html',{'title':'Register Page','form':form,})
    return render(request,'website/register.html',{'title':'Register Page','form':form,})


 


def book_detail(request, pk):
    if request.user.is_authenticated:
        book = Book.objects.get(id = pk)
        return render(request,'website/record.html',{'book':book})
    else:
        messages.success(request, "You Must Be logged In to View these Records")
        return redirect('website:home')
    




def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Book.objects.get(id=pk)
        record.delete()
        messages.success(request, "The Recored Has Been Deleted Successfully")
        return redirect('website:home')
    else:
        messages.success(request, "You Must Be logged In to Delte this Record")
        return redirect('website:home')







def add_record(request):
    form = AddRecord(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Your Record Has Been Created!...")
                return redirect('website:home')
            
        return render(request, 'website/add_record.html',{'form':form})
    else:
        messages.success(request, "You Must Be logged In to Delte this Record")
        return redirect('website:home')





def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Book.objects.get(id=pk)
        form = AddRecord(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Record Has Been Updated!...")
            return redirect('website:home')
        return render(request, 'website/update_record.html',{'form':form})
    else:
        messages.success(request, "You Must Be logged In to Delte this Record")
        return redirect('website:home') 
    


# from .models import Student
# from django.http import HttpResponseRedirect
# def my_login(request):
#     if request.method == 'POST':
#         usernm=request.POST['username']
#         passwd=request.POST['password']
#         obj = Student.objects.filter(username=usernm, password=passwd)[0]
#         if obj is not None:
#             return redirect('website:stu_dash')
#         else:
#             messages.success(request,'invalid')
#     else:
#         return render(request,'website/stu_login.html')        







# Your views.py
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def student_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('stu_dash')  # Redirect to the dashboard or any other desired page
    else:
        form = AuthenticationForm()

    return render(request, 'website/login.html', {'form': form})







def stu_dash(request,pk):
    student = Student.objects.get(id=pk)
    return render(request,'website/stu_dash.html',{'student':student})



from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentRegistrationForm  # You'll need to create this form

from django.urls import reverse

def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            new_student = form.save()

            # Get the pk of the newly registered student
            new_student_pk = new_student.pk  # Assuming pk is the primary key of your Student model

            # Construct the URL for the student's dashboard
            dashboard_url = reverse('website:std_dash', args=[new_student_pk])

            # Optionally, you can log the user in here
            return redirect(dashboard_url)  # Redirect to the student's dashboard after successful registration
    else:
        form = StudentRegistrationForm()

    return render(request, 'website/register.html', {'form': form})









# views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomLoginForm  # Import your custom login form

from django.urls import reverse

def custom_login(request):
    if request.method == 'POST':
        usernm = request.POST['username']
        passwd = request.POST['password']
        obj = Student.objects.get(username=usernm, password=passwd)
        if obj is not None:
            # Get the student's pk and construct the URL for their dashboard
            pk = obj.pk  # Assuming pk is the primary key of your Student model
            dashboard_url = reverse('website:std_dash', args=[pk])
            return redirect(dashboard_url)
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('website:std_login')

    return render(request, 'website/stu_login.html')
