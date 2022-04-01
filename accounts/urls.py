from django.urls import path
from accounts import views

urlpatterns = [
    path('student-sign-up/',views.student_signup_view,name='student_signup'),
    path('teacher-sign-up/',views.teacher_signup_view,name='teacher_signup'),
    path('teacher-view/',views.teacher_view,name="teacher_view"),
    path('student-view/',views.student_view,name="student_view"),
    path('redirect-view',views.redirect_user_view,name="redirect_user"),
    path('',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
]