from django.shortcuts import render
from django.views import View


class ResumePage(View):
    '''
    The main logic for just render staic html page
    '''

    def get(self, request):
        return render(request, 'resume/resume.html')
