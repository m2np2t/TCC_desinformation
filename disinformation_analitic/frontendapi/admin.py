from django.contrib import admin

# Register your models here.

from .models import User, Disinformation

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 
                    'email', 
                    'password')


    list_display_links = ('name', 'email', 'password')
    #list_filter = ('id', 'name', 'email')
    list_per_page = 10
    search_fields = ('id', 'name', 'email')
    list_editable = ()

class DisinformationAdmin(admin.ModelAdmin):
    list_display = ('auto_increment_id',
                    'key', 
                    'link', 
                    'text',
                    'title',
                    'user')

    list_display_links = ('auto_increment_id', 'key', 'link', 'text', 'title','user')
    #list_filter = ('auto_increment_id', 'key', 'user')
    list_per_page = 10
    search_fields = ('auto_increment_id', 'key', 'user')
    list_editable = ()

admin.site.register(User, UserAdmin)
admin.site.register(Disinformation, DisinformationAdmin)