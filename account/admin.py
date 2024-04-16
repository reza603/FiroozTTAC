from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms  import CustomUserChangeForm,CustomUserCrerationForm
from .models import CustomUser



class CudtomUserAdmin(UserAdmin):
    add_form=CustomUserCrerationForm
    form=CustomUserChangeForm
    model=CustomUser
    fieldsets= UserAdmin.fieldsets + (
        (None,{'fields':('AccessLevel' ,)}),
    )
    
  
    add_fieldsets= UserAdmin.add_fieldsets + (
         (None,{'fields':('AccessLevel' ,)}),
    )
    
admin.site.register(CustomUser,CudtomUserAdmin)