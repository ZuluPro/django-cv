from django.utils.translation import ugettext_lazy as _


def export_resume(modeladmin, request, queryset):
    pass
export_resume.short_description = _("Export resume as PDF")
