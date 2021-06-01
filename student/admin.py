from django.contrib import admin
from .models import Registration,Subscribe,Admission,Contact,Comment,Fqu,Cart,Cources,Specific_Crc
# Register your models here.
admin.site.register([Registration,Subscribe,Admission,Contact,Comment,Fqu,Cources,Cart,Specific_Crc])