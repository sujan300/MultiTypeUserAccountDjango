from django import forms
from accounts.models import Account,Student,gender_choices,Teacher
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


'''
    this is teacher registration form 
'''

class StudentCreationForm(UserCreationForm):
    GENDER = (
        ('Male','Male'),
        ('Female','Female')
    )

    gender = forms.ChoiceField(
            choices=GENDER,
            widget=forms.Select(attrs={
                'class':'form-control'
        }))


    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder':'Password',
            'class':'form-control',
        }))


    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password(again)',
        'class':'form-control',
    }))


    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={
            'placeholder':'yyy/mmm/ddd',
            'class':'form-control',
            'type':'date'
        })
    )

    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ['first_name','last_name','phone_number','email']


        widgets     = {
            'first_name':forms.TextInput(attrs={'placeholder':'First Name','class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Phone Number'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email'}),
        }


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.is_active  = True
        user.save()
        student = Student.objects.create(user=user)
        student.gender = self.cleaned_data.get('gender')
        student.date_of_birth = self.cleaned_data.get('date_of_birth')
        print("self.date_of_birth",self.cleaned_data.get('date_of_birth'))
        student.save()
        return user






'''
    this is for teacher registration form
'''

class TeacherCreactionForm(UserCreationForm):
    GENDER = (
        ('Male','Male'),
        ('Female','Female')
    )

    gender = forms.ChoiceField(
            choices=GENDER,
            widget=forms.Select(attrs={
                'class':'form-control'
        }))


    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder':'Password',
            'class':'form-control',
        }))


    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password(again)',
        'class':'form-control',
    }))


    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ['first_name','last_name','phone_number','email']


        widgets     = {
            'first_name':forms.TextInput(attrs={'placeholder':'First Name','class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Phone Number'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email'}),
        }


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.is_active = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.gender = self.cleaned_data.get('gender')
        teacher.save()
        return user