from django.contrib import admin
from app.models import WebPage, Topic, AccessRecord

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(WebPage)
