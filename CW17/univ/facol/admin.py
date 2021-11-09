from django.contrib import admin
from .models import Facolty
from .models import Prof
from .models import Lesson
from .models import Student


# Register your models here.


admin.site.register(Facolty)
admin.site.register(Prof)
admin.site.register(Lesson)
admin.site.register(Student)
