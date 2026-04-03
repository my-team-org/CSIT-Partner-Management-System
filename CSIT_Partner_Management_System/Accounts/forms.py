from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from Core.models import Student

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # เพิ่มผู้ใช้เข้า Group ชื่อ 'student'
            group, created = Group.objects.get_or_create(name='student')
            user.groups.add(group)

            # สร้าง Student พร้อมกับ User
            Student.objects.create(
                user=user,
        
                student_id=self.cleaned_data['username'],
            )
        return user
