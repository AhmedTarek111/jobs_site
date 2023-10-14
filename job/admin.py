from django.contrib import admin
from .models import JobEducation_Experience,Jobs,JobRequiredSkills
# Register your models here.
class InlineEducation(admin.TabularInline):
    model =JobEducation_Experience

class InlineJobRequiredSkills(admin.TabularInline):
    model =JobRequiredSkills

class JobAdmin(admin.ModelAdmin):
    inlines =[InlineEducation,InlineJobRequiredSkills]


admin.site.register(Jobs,JobAdmin)
admin.site.register(JobEducation_Experience)
admin.site.register(JobRequiredSkills)  


