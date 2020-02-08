from django.shortcuts import render
from django.views.generic import ListView, View


class Dashboard(View):
    dashboard_template = 'SMdashboard/dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.dashboard_template)

    def post(self, request, *args, **kwargs):
        return render(request, self.dashboard_template)
