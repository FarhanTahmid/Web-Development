from django.contrib import admin

# Register your models here.
from .models import OfferedCourse
from .models import Grade
from .models import Complains
from .models import Image
admin.site.register(Grade)
admin.site.register(OfferedCourse)
admin.site.register(Complains)
admin.site.register(Image)