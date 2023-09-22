from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecord
from .models import Book
# Create your views here.


def home(request):
    books = Book.objects.all()




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
        return render(request, 'website/home.html', {'title':'Home Page', 'books':books})




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