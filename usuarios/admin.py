from django.contrib import admin
from .models import UserAbs
from django.contrib.auth.admin import UserAdmin

class UserAbsAdmin(UserAdmin):
    list_display  = ('username','password', 'telefone', 'is_staff')
    fieldsets = UserAdmin.fieldsets + ((None , {'fields' : ('telefone',)}))
    add_fieldsets = UserAdmin.add_fieldsets + ((None , {'fields' : ('telefone',)}))

admin.site.register(UserAbs)