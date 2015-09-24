from django.contrib import admin
from curriculum.models.certification import Certification, CertificationItem
from curriculum.models.experience import Experience
from curriculum.models.language import Language, LanguageItem
from curriculum.models.project import Project, ProjectItem
from curriculum.models.resume import Resume
from curriculum.models.skill import Skill, SkillItem
from curriculum.models.training import Training


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'title', 'tags')
    fieldsets = (
        (None, {
            'fields': (
                ('firstname', 'lastname', 'title'),
                ('resume', 'image'),
                ('phone', 'email'),
                'address',
                ('driving_license', 'hobbies'),
                'tags'
            )
        }),
    )


class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'authority')
    fieldsets = (
        (None, {
            'fields': (
                ('title', 'authority', 'url'),
                'description',
            )
        }),
    )


class CertificationItemAdmin(admin.ModelAdmin):
    list_display = ('certification', 'resume')
    fieldsets = (
        (None, {
            'fields': (
                'resume',
                'certification',
                ('start_year', 'start_month', 'expires'),
                ('end_year', 'end_month'),
            )
        }),
    )


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'entreprise', 'resume')
    fieldsets = (
        (None, {
            'fields': (
                'resume',
                ('title', 'entreprise', 'type'),
                'description',
                ('start_year', 'start_month', 'still'),
                ('end_year', 'end_month'),
            )
        }),
    )


class LanguageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
    )


class LanguageItemAdmin(admin.ModelAdmin):
    list_display = ('language', 'level', 'resume')
    fieldsets = (
        (None, {
            'fields': (
                'resume',
                ('language', 'level'),
            )
        }),
    )


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    fieldsets = (
        (None, {
            'fields': (
                ('title', 'url'),
                'description',
            )
        }),
    )


class ProjectItemAdmin(admin.ModelAdmin):
    list_display = ('project', 'resume')
    fieldsets = (
        (None, {
            'fields': (
                'resume',
                'project',
                'contribution',
                ('start_year', 'start_month', 'still'),
                ('end_year', 'end_month')
            )
        }),
    )


class SkillAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
    )


class SkillItemAdmin(admin.ModelAdmin):
    list_display = ('skill', 'level', 'resume')
    fieldsets = (
        (None, {
            'fields': (
                'resume',
                ('skill', 'level'),
            )
        }),
    )


class TrainingAdmin(admin.ModelAdmin):
    list_display = ('degree', 'school', 'topic', 'resume')
    fieldsets = (
        (None, {
            'fields': (
                'resume',
                ('degree', 'school', 'topic'),
                'result',
                ('year', 'month'),
                'description'
            )
        }),
    )


admin.site.register(Resume, ResumeAdmin)
admin.site.register(Certification, CertificationAdmin)
admin.site.register(CertificationItem, CertificationItemAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(LanguageItem, LanguageItemAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectItem, ProjectItemAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(SkillItem, SkillItemAdmin)
admin.site.register(Training, TrainingAdmin)
