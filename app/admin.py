from django.contrib import admin
from .models import DollarCourse


class DollarCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'dollar_course', 'som_input', 'dollar_input', 'dollar', 'som', 'created')
    list_display_links = ('id', 'dollar_course')
    list_filter = ('created', )


admin.site.register(DollarCourse, DollarCourseAdmin)
