from django.contrib import admin
from Elearn.models import Subject,Enroll,Content,files
# Register your models here.
admin.site.register(Subject)
admin.site.register(Enroll)
admin.site.register(Content)
admin.site.register(files)