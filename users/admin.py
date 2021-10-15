#contains function avalible when logged in as an admin 
#allows the admin to view user profiles 
from django.contrib import admin
from . models import UserProfile


# DOCS - https://docs.djangoproject.com/en/3.1/ref/contrib/admin/

class UserProfileAdmin(admin.ModelAdmin):
	
	list_display = ('id', 'user', 'timestamp')

admin.site.register(UserProfile,UserProfileAdmin)