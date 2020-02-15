from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # override get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()
        context['clients'] = Client.objects.all()
        return context

    def post(self, request):
        if request.method == 'POST':
            message = request.POST['message']
            name = request.POST['name']
            email = request.POST['email']
            context = {'name': name, 'email': email, 'message': message}
            template = render_to_string('email_template.html', context)

            send_mail('Contact Form',
                      template,
                      settings.EMAIL_HOST_USER,
                      ['lecorffpierre@gmail.com'],
                      fail_silently=False)
        return render(request, 'home.html', self.get_context_data())
