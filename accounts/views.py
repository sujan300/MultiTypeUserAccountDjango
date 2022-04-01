from django.shortcuts import render,HttpResponse,redirect
from accounts.forms import StudentCreationForm,TeacherCreactionForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from accounts.decorators import student_required,teacher_required

# Create your views here.
def student_signup_view(request):
    if request.method == "POST":
        print("yes POst Request !!!")
        form = StudentCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>registration completed !</h1>")
    else:
        form = StudentCreationForm()
    context = {
        'form':form,
    }
    return render(request,'student_registration.html',context)


# teacher2@gmail.com

def teacher_signup_view(request):
    if request.method == "POST":
        print("yes POst Request !!!")

        print("password1",request.POST.get('password1'))
        print("password2",request.POST.get('password2'))
        form = TeacherCreactionForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>registration completed !</h1>")
    else:
        form = TeacherCreactionForm()
    context = {
        'form':form,
    }
    return render(request,'teacher_registration.html',context)

def login_view(request):
    if request.method =="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email,password=password)
        print(user)
        if user:
            login(request, user)
            print("teacher and student check")
            print(user.is_teacher)
            print(user.is_student)

            if user.is_teacher:
                return redirect('teacher_view')
            elif user.is_student:
                return redirect('student_view')
    return render(request, 'login.html')


@teacher_required
@login_required
def teacher_view(request):
    return render(request, 'teacher.html')




@student_required
@login_required
def student_view(request):
    return render(request, 'student.html')


@login_required
def redirect_user_view(request):
    return render(request, 'redirect_user.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')