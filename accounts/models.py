from django.db import models
from django.contrib.auth.base_user import BaseUserManager,AbstractBaseUser
# Create your models here.



gender_choices=(
    ('Male','Male'),
    ("Female","Female"),
)



class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,phone_number,email,password=None):
        if not email:
            raise ValueError("user must have an email account !")
        user=self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name  = last_name,
        )
        user.set_password(password)
        user.phone_number = phone_number
        user.save(using = self._db)
        return user



    def create_superuser(self,first_name,last_name,email,phone_number,password=None):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            password=password
        )


        user.is_admin       = True
        user.is_staff       = True
        user.is_active      = True
        user.is_superadmin  = True

        user.save(using=self._db)
        return user





class Account(AbstractBaseUser):
    first_name      = models.CharField(max_length=100)
    last_name       = models.CharField(max_length=100)
    email           = models.EmailField(max_length=50,unique=True)
    phone_number    = models.CharField(max_length=20,unique=True)

    # required 
    date_joined  = models.DateTimeField(auto_now_add=True)
    last_login   = models.DateTimeField(auto_now_add=True)
    is_admin     = models.BooleanField(default=False)
    is_staff     = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=False)
    is_superadmin= models.BooleanField(default=False)

    # addtional information 

    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    USERNAME_FIELD  ="email"
    REQUIRED_FIELDS =['first_name','last_name','phone_number']

    objects         = MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,add_label):
        return True


class Student(models.Model):
    gender          = models.CharField(max_length=11)
    user            = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_of_birth   = models.DateField(blank=True,null=True)




class Teacher(models.Model):
    gender         = models.CharField(max_length=11)
    user           = models.ForeignKey(Account, on_delete=models.CASCADE)
