from django.shortcuts import render
from .models import Project, Job

# Create your views here.
def home(request):
    jobs = Job.objects.all().order_by('-start_date')
    projects = Project.objects.all().order_by('-date_complete')
    top3_jobs = Job.objects.all().order_by('-start_date')[:3]
    top3_projects = Project.objects.all().order_by('-date_complete')[:3]
    job_count = jobs.count()
    proj_count = projects.count()

    ctx = { 'jobs':jobs,
            'projects':projects,
            'proj_count':proj_count,
            'job_count':job_count,
            'top3_jobs':top3_jobs,
            'top3_projects':top3_projects}


    # if jobs.count() >= 3:
    #     latest_job = Job.objects.all().order_by('-start_date')[0]
    #     second_latest_job = Job.objects.all().order_by('-start_date')[1]
    #     third_latest_job = Job.objects.all().order_by('-start_date')[2]
    #     ctx['latest_job'] = latest_job
    #     ctx['second_latest_job'] = second_latest_job
    #     ctx['third_latest_job'] = third_latest_job
    #
    # elif jobs.count() >= 2:
    #     latest_job = Job.objects.all().order_by('-start_date')[0]
    #     second_latest_job = Job.objects.all().order_by('-start_date')[1]
    #     ctx['latest_job'] = latest_job
    #     ctx['second_latest_job'] = second_latest_job
    # elif jobs.count() >= 1:
    #     latest_job = Job.objects.all().order_by('-start_date')[0]
    #     ctx['latest_job'] = latest_job
    #
    #
    #
    # if projects.count() >= 3:
    #     latest_proj = Project.objects.all().order_by('-date_complete')[0]
    #     second_latest_proj = Project.objects.all().order_by('-date_complete')[1]
    #     third_latest_proj = Project.objects.all().order_by('-date_complete')[2]
    #     ctx['latest_proj'] = latest_proj
    #     ctx['second_latest_proj'] = second_latest_proj
    #     ctx['third_latest_proj'] = third_latest_proj
    # elif projects.count() >= 2:
    #     latest_proj = Project.objects.all().order_by('-date_complete')[0]
    #     second_latest_proj = Project.objects.all().order_by('-date_complete')[1]
    #     ctx['latest_proj'] = latest_proj
    #     ctx['second_latest_proj'] = second_latest_proj
    # elif projects.count() >= 1:
    #     latest_proj = Project.objects.all().order_by('-date_complete')[0]
    #     ctx['latest_proj'] = latest_proj

    return render(request, 'portfolio_app/home.html', ctx)

def jobs(request):
    jobs = Job.objects.all()
    return render(request, 'portfolio_app/jobs.html', {'jobs':jobs})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio_app/projects.html', {'projects':projects})

def about(request):
    return render(request, 'portfolio_app/about.html')


def project_overview(request):
    return render(request, 'portfolio_app/project_overview.html')
