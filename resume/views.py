from django.shortcuts import render, redirect
from .forms import ResumeForm, EducationForm, WorkExperienceForm, HobbyForm
from .models import Resume, Education, Hobby, WorkExperience

# Create your views here.
def new_resume(request):
    resumes = Resume.objects.all().order_by('-id')[:5]
    if request.method == 'POST':
        form = ResumeForm(data=request.POST)
        if form.is_valid():            
            resume_ = form.save()
            return redirect(f'resume/{resume_.id}')
        else:
            return render(request, 'new_resume.html', {'form': form, 'resumes': resumes})
    else:
        form = ResumeForm()
        return render(request, 'new_resume.html', {'form': form, 'resumes': resumes})

def view_resume(request, id):
    resume = Resume.objects.get(id=id)
    educations = Education.objects.filter(resume=resume).order_by('id')
    work_experiences = WorkExperience.objects.filter(resume=resume).order_by('id')
    hobbies = Hobby.objects.filter(resume=resume).order_by('id')

    if request.method == 'POST':
        if request.POST.get("education"):
            
            if request.POST.get("delete"):
                record = Education.objects.get(id=request.POST.get("delete"))
                record.delete()
                return redirect(f'/resume/{resume.id}')

            education = EducationForm(resume=resume, data=request.POST)
            if education.is_valid():
                education.save()
                return redirect(f'/resume/{resume.id}')
            else:
                return render(request, 'view_resume.html',{
                    'cv': resume,
                    'resume_form': ResumeForm(),
                    'education_form': education,
                    'work_experience_form': WorkExperienceForm(resume=None),
                    'hobby_form': HobbyForm(resume=None),
                    'educations': educations,
                    'work_experiences': work_experiences,
                    'hobbies': hobbies
                })
        elif request.POST.get("work"):
            
            if request.POST.get("delete"):
                record = WorkExperience.objects.get(id=request.POST.get("delete"))
                record.delete()
                return redirect(f'/resume/{resume.id}')

            work = WorkExperienceForm(resume=resume, data=request.POST)
            if work.is_valid():
                work.save()
                return redirect(f'/resume/{resume.id}')
            else:
                return render(request, 'view_resume.html',{
                    'cv': resume,
                    'resume_form': ResumeForm(),
                    'education_form': EducationForm(resume=None),
                    'work_experience_form': work,
                    'hobby_form': HobbyForm(resume=None),
                    'educations': educations,
                    'work_experiences': work_experiences,
                    'hobbies': hobbies
                })
        elif request.POST.get("hobby"):
            if request.POST.get("delete"):
                record = Hobby.objects.get(id=request.POST.get("delete"))
                record.delete()
                return redirect(f'/resume/{resume.id}')

            hobby = HobbyForm(resume=resume, data=request.POST)
            if hobby.is_valid():
                hobby.save()
                return redirect(f'/resume/{resume.id}')
            else:
                return render(request, 'view_resume.html',{
                    'cv': resume,
                    'resume_form': ResumeForm(),
                    'education_form': EducationForm(resume=None),
                    'work_experience_form': WorkExperienceForm(resume=None),
                    'hobby_form': hobby,
                    'educations': educations,
                    'work_experiences': work_experiences,
                    'hobbies': hobbies
                })
        else:
            form = ResumeForm(data=request.POST, instance=resume)
            if form.is_valid():            
                resume_ = form.save()
                return redirect(f'/resume/{resume_.id}')
            else:
                return render(request, 'view_resume.html',{
                    'cv': resume,
                    'resume_form': form,
                    'education_form': EducationForm(resume=None),
                    'work_experience_form': WorkExperienceForm(resume=None),
                    'hobby_form': HobbyForm(resume=None),
                    'educations': educations,
                    'work_experiences': work_experiences,
                    'hobbies': hobbies
                })
    else:
        return render(request, 'view_resume.html',{
            'cv': resume,
            'resume_form': ResumeForm(instance=resume),
            'education_form': EducationForm(resume=None),
            'work_experience_form': WorkExperienceForm(resume=None),
            'hobby_form': HobbyForm(resume=None),
            'educations': educations,
            'work_experiences': work_experiences,
            'hobbies': hobbies
        })