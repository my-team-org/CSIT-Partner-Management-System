from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login  # เปลี่ยนชื่อ import
from .forms import RegisterForm, LoginForm

def index(request):
    return render(request, 'registration/home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # ใช้ auth_login แทน
            return redirect('core:home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):  # เปลี่ยนชื่อฟังก์ชันนี้
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)  # ใช้ auth_login แทน
                # เช็คว่า User อยู่ใน Group ไหน แล้วส่งไปยังหน้า Dashboard ที่ถูกต้อง
                if user.groups.filter(name="student").exists():
                    return redirect("core:home")
                elif user.groups.filter(name="HR").exists():
                    return redirect("core:home")
                elif user.groups.filter(name="CSIT").exists():
                    return redirect("core:home")
                else:
                    return redirect("accounts:login")  # ถ้าไม่มี Group ให้กลับไปหน้า Login
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})