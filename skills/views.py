from django.shortcuts import render

# Create your views here.
from .models import AdminSkill
def admin_skills(request):
    code_skill = AdminSkill.objects.all().filter(title = 'code')
    design_skill = AdminSkill.objects.all().filter(skill_name = 'design')
    print("============================================")
    # print(code_skill)
    context = {
        'code_skills':code_skill,
        'design_skills':design_skill,

    }

    return render(request, 'home_page2.html', context)