from django.shortcuts import render, redirect
from .forms import ResumeForm
from .models import Resume

# Create your views here.
def new_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():            
            resume_ = form.save()
            redirect(f'resume/{resume_}')
    else:
        form = ResumeForm()
        return render(request, 'new_resume.html', {'form': form})

def view_resume(request, id):
    pass