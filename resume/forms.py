from django.forms import ModelForm
from .models import Resume, Education, WorkExperience, Hobby

class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = [
            'display_name',
            'email',
            'date_of_birth',
            'phone_number',
            'personal_summary'
        ]



class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            'school_name',
            'school_start_date',
            'school_end_date',
            'best_subject',

        ]

class WorkExperienceForm(ModelForm):
    class Meta:
        model = WorkExperience
        fields = [
            'job_role_or_title',
            'company',
            'job_description',
            'job_start_date',
            'job_end_date'
        ]

class HobbyForm(ModelForm):
    class Meta:
        model = Hobby
        fields = [
            'interest_or_hobby'
        ]