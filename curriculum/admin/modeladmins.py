from django.contrib import admin
from curriculum import models, forms
from curriculum.admin import actions


class ResumeAdmin(admin.ModelAdmin):
    actions = (actions.export_resume,)
    list_display = ('firstname', 'lastname', 'title', 'tags')
    fieldsets = (
        (None, {
            'fields': (
                ('firstname', 'lastname', 'title'),
                ('resume', 'image'),
                ('phone', 'email', 'website'),
                ('country', 'city', 'address'),
                'skill_summary',
                'experience_summary',
                'training_summary',
                'project_summary',
                ('linkedin', 'skype', 'stackoverflow', 'github', 'google'),
                ('driving_license', 'hobbies'),
                'tags',
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
    form = forms.ExperienceForm
    list_display = ('title', 'entreprise', 'start_year', 'start_month',
                    'end_year', 'end_month',
                    'resume', 'weight')
    fieldsets = (
        (None, {
            'fields': (
                'resume',
                ('title', 'entreprise', 'type'),
                'context',
                'description',
                'results',
                'environment',
                ('start_year', 'start_month', 'still'),
                ('end_year', 'end_month'),
                'weight',
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
                ('end_year', 'end_month'),
                'weight'
            )
        }),
    )


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'tags')
    list_per_page = 200
    fieldsets = (
        (None, {
            'fields': (
                ('name', 'url'),
                'description',
                ('color', 'tags')
            )
        }),
    )


class SkillItemAdmin(admin.ModelAdmin):
    list_display = ('skill', 'level', 'category', 'resume', 'weight')
    list_per_page = 200
    fieldsets = (
        (None, {
            'fields': (
                'resume',
                ('skill', 'level', 'category'),
                ('start_year', 'start_month'),
                'weight'
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


admin.site.register(models.Resume, ResumeAdmin)
admin.site.register(models.Certification, CertificationAdmin)
admin.site.register(models.CertificationItem, CertificationItemAdmin)
admin.site.register(models.Experience, ExperienceAdmin)
admin.site.register(models.Language, LanguageAdmin)
admin.site.register(models.LanguageItem, LanguageItemAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.ProjectItem, ProjectItemAdmin)
admin.site.register(models.Skill, SkillAdmin)
admin.site.register(models.SkillItem, SkillItemAdmin)
admin.site.register(models.Training, TrainingAdmin)
