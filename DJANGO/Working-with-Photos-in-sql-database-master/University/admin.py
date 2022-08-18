from django.contrib import admin

# Register your models here.
from .models import OfferedCourse
from .models import Grade
from .models import Complains

admin.site.register(Grade)
admin.site.register(OfferedCourse)
admin.site.register(Complains)