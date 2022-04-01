from django.contrib import admin
from accounts.models import Account,Student,Teacher
# Register your models here.

class AdminAccount(admin.ModelAdmin):
    list_display = ["id","email","phone_number","first_name","last_name","is_student","is_teacher"]
    list_display_links  = ['first_name','email']
admin.site.register(Account,AdminAccount)


class StudentAdmin(admin.ModelAdmin):
    list_display = ["gender","user","date_of_birth"]
admin.site.register(Student,StudentAdmin)



class TeacherAdmin(admin.ModelAdmin):
    list_display = ["gender","user"]
admin.site.register(Teacher,TeacherAdmin)
