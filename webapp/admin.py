from django.contrib import admin
from models import *
from django import forms
from django.contrib.auth.models import User


# Register your models here.


class UserProfileInline(admin.TabularInline):
    model = UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    #     models.CharField: {'widget': TextInput(attrs={'size':'40'})},
    #     }
    save_on_top = True
    #    readonly_fields = ('message_back', 'date_read', 'date_create',)
    list_display = ('user', 'phone', 'mobile', )
    #list_editable = ('favourite',)
    #list_filter = ('favourite',)
   # search_fields = ['name', 'shortname',]
    #readonly_fields = ('coin', 'coinChange', 'exchange', 'price', 'vol', 'lastUpdate', 'listChart')
    #raw_id_fields = ('router', )
    #inlines = [UserProfileInline, ]
    #fieldsets = [
    #    (None, {'fields': ['coin', 'coinChange', 'exchange', 'price', 'vol', 'lastUpdate', 'listChart']}),
    #    ]

admin.site.register(UserProfile, UserProfileAdmin)

# admin.site.unregister(User)
# admin.site.register(User, UserProfileAdmin)