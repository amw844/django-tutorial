from django.forms import ModelForm, DateField, DateInput
from .models import Resume, Education, WorkExperience, Hobby

class ResumeForm(ModelForm):
    date_of_birth = DateField(widget=DateInput(format = '%d/%m/%Y'), 
                                 input_formats=('%d/%m/%Y',))

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
    
    def __init__(self, resume, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.resume = resume
    
    school_start_date = DateField(widget=DateInput(format = '%d/%m/%Y'), 
                                 input_formats=('%d/%m/%Y',))
    school_end_date = DateField(widget=DateInput(format = '%d/%m/%Y'), 
                                 input_formats=('%d/%m/%Y',))

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

    def __init__(self, resume, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.resume = resume
    
    job_start_date = DateField(widget=DateInput(format = '%d/%m/%Y'), 
                                 input_formats=('%d/%m/%Y',))
    job_end_date = DateField(widget=DateInput(format = '%d/%m/%Y'), 
                                 input_formats=('%d/%m/%Y',))

class HobbyForm(ModelForm):
    class Meta:
        model = Hobby
        fields = [
            'interest_or_hobby'
        ]

    def __init__(self, resume, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.resume = resume