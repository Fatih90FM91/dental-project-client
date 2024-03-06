from django.contrib import admin
from .models import Register

class RegisterAdmin(admin.ModelAdmin):
    register_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'city')
    register_display_links = ('id', 'first_name')
    register_filter = ('first_name', )
    register_editable = ('add_member',)
    register_fields = ('first_name', 'question', 'date_of_birth', 'city', 'state', 'zipcode', 'street')
    register_per_page = 25


admin.site.register(Register, RegisterAdmin)