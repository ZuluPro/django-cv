from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import widgets
from django.contrib.staticfiles.templatetags.staticfiles import static
from curriculum import models


class ResumeExportForm(forms.Form):
    hide_image = forms.BooleanField()
    hide_resume = forms.BooleanField()

    hide_phone = forms.BooleanField()
    hide_city = forms.BooleanField()
    hide_country = forms.BooleanField()
    hide_address = forms.BooleanField()

    hide_email = forms.BooleanField()
    hide_website = forms.BooleanField()
    hide_skype = forms.BooleanField()
    hide_twitter = forms.BooleanField()
    hide_linkedin = forms.BooleanField()
    hide_stackoverflow = forms.BooleanField()
    hide_github = forms.BooleanField()
    hide_experience_description = forms.BooleanField()
    hide_experience_environment = forms.BooleanField()
    hide_certification_description = forms.BooleanField()
    hide_training_description = forms.BooleanField()
    hide_project_contribution = forms.BooleanField()
    hide_project_url = forms.BooleanField()

    class Media:
        css = {'all': (static('admin/css/widgets.css'),), }

    def __init__(self, instance, *args, **kwargs):
        super(ResumeExportForm, self).__init__(*args, **kwargs)
        self.instance = instance
        self.fields['experiences'] = forms.ModelMultipleChoiceField(
            queryset=instance.experiences.all(),
            initial=instance.experiences.all(),
            widget=widgets.FilteredSelectMultiple(_("experiences"), is_stacked=False,
                    attrs={'size': 5, 'style': 'height: unset'}))
        self.fields['projects'] = forms.ModelMultipleChoiceField(
            queryset=instance.projects.all(),
            initial=instance.projects.all(),
            widget=widgets.FilteredSelectMultiple(_("projects"), is_stacked=False,
                    attrs={'size': 5, 'style': 'height: unset'}))
        self.fields['skills'] = forms.ModelMultipleChoiceField(
            queryset=instance.skills.order_by('skill__name'),
            initial=instance.skills.all(),
            widget=widgets.FilteredSelectMultiple(_("skills"), is_stacked=False,
                    attrs={'size': 5, 'style': 'height: unset'}))
        self.fields['certifications'] = forms.ModelMultipleChoiceField(
            queryset=instance.certifications.all(),
            initial=instance.certifications.all(),
            widget=widgets.FilteredSelectMultiple(_("certifications"), is_stacked=False,
                    attrs={'size': 5, 'style': 'height: unset'}))
        self.fields['trainings'] = forms.ModelMultipleChoiceField(
            queryset=instance.trainings.all(),
            initial=instance.trainings.all(),
            widget=widgets.FilteredSelectMultiple(_("trainings"), is_stacked=False,
                    attrs={'size': 3, 'style': 'height: unset'}))
        self.fields['languages'] = forms.ModelMultipleChoiceField(
            queryset=instance.languages.all(),
            initial=instance.languages.all(),
            widget=widgets.FilteredSelectMultiple(_("languages"), is_stacked=False,
                    attrs={'size': 4, 'style': 'height: unset'}))


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = models.Experience
        exclude = ()

    def clean(self):
        cleaned_data = super(ExperienceForm, self).clean()
        if cleaned_data.get('end_month') and not cleaned_data.get('end_year'):
            raise forms.ValidationError(_(
                "You must specify an end year with end month."))
        if cleaned_data.get('end_year'):
            if cleaned_data.get('end_year') < cleaned_data.get('start_year'):
                raise forms.ValidationError(_("End year is lower than start."))
        if cleaned_data.get('end_year') == cleaned_data.get('start_year'):
            if cleaned_data.get('end_month') < cleaned_data.get('start_month'):
                raise forms.ValidationError(_("End month is lower than start."))

    def clean_end_year(self):
        data = self.cleaned_data['end_year']
        if not self.cleaned_data['still'] and not data:
            raise forms.ValidationError(_(
                "You must specify an end year if experience is finished."))
        return data
