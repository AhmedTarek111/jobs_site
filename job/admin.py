from django.contrib import admin
from .models import JobEducation_Experience,Jobs,JobRequiredSkills
# Register your models here.
class InlineEducation(admin.TabularInline):
    model =JobEducation_Experience

class JobEducationdAdmin(admin.ModelAdmin):
    inlines =[InlineEducation,]


class InlineJobRequiredSkills(admin.TabularInline):
    model =JobRequiredSkills

class JobRequiredSkillsAdmin(admin.ModelAdmin):
    inlines =[InlineJobRequiredSkills,]


admin.site.register(Jobs,JobRequiredSkillsAdmin)
admin.site.register(JobEducation_Experience)
admin.site.register(JobRequiredSkills)  


