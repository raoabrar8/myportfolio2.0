from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.mail import send_mail
# Create your views here.
def HomeView(request):
    abouts = AboutModel.objects.all()
    jobes = JobModel.objects.all()
    testimonials = TestimonialsModel.objects.all()
    clients = ClinetsModel.objects.all()
    educations = EducationModel.objects.all()
    experiences = ExperineceModel.objects.all()
    certificates = CertficateModel.objects.all()
    skills = SkillsModel.objects.all()
    projects = ProjectModel.objects.all()
    blogs = BlogModel.objects.all()
    categories = CatrgoryModel.objects.all()
    profiles = ProfileModel.objects.all()
    contacts = ShowContactsModel.objects.all()
    socials = SocialModel.objects.all()
    cvs = CvModel.objects.all()
    f_skills = FrontendSkillModel.objects.all()
    b_skills = BackendSkillModel.objects.all()
    ai_skills = AISkillModel.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            your_message = form.cleaned_data['your_message']

            send_mail(
                f"New message from {full_name}",
                f"Message: {your_message}\n\nFrom: {full_name} <{email}>",
                email,  # From email
                ['raoabrarn@gmail.com'],  # To email
                fail_silently=False,
            )
            
            return redirect('home')
    else:
        form = ContactForm()
    context = {'form' : form, 
               'abouts' : abouts,
               'jobes' : jobes, 
                'testimonials': testimonials, 
                'clients': clients,
                'educations': educations, 
                'experiences' : experiences, 
                'certificates': certificates, 
                'skills': skills, 
                'projects' : projects, 
                'blogs': blogs,
                'categories' : categories,
                'profiles': profiles, 
                'contacts': contacts,
                'socials': socials,
                'cvs'  : cvs,
                'f_skills' : f_skills,
                'b_skills' : b_skills,
                'ai_skills': ai_skills}
    return render(request, 'Home.html', context)