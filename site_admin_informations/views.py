from django.shortcuts import render

# Create your views here.
from .models import AdminInformation
from skills.models import AdminSkill
from site_educations.models import Education
from site_experiences.models import Experience
from site_services.models import Service
from site_members.models import Member
from site_contact.models import Contact
from site_contact.forms import FormContact
def admin_informations(request):
    #for info
    admin_info = AdminInformation.objects.get(active = True)

    # for skills
    code_skill = AdminSkill.objects.all().filter(title = 'code')
    design_skill = AdminSkill.objects.all().filter(title = 'design')
    
    #for Educations
    education = Education.objects.all()

    #for Experiences
    experience = Experience.objects.all()

    #for Services
    service = Service.objects.all()

    #for Members
    member = Member.objects.all()

    #for contact
    form_contact = FormContact(request.POST or None)
    if form_contact.is_valid():
        full_name = form_contact.cleaned_data.get('full_name')
        email = form_contact.cleaned_data.get('email')
        subject = form_contact.cleaned_data.get('subject')
        message = form_contact.cleaned_data.get('message')
        Contact.objects.create(full_name = full_name,email = email,subject = subject,message = message, is_read = False)
        form_contact = Contact()


    context = {
        'admin_info':admin_info,
        'code_skills':code_skill,
        'design_skills':design_skill,
        'educations':education,
        'experiences': experience,
        'services': service,
        'members': member,
        'form':form_contact,
    }

    return render(request, 'home_page2.html', context)


# def contact(request):
#     form