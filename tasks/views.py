from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render
from django.template import Context, loader
from .models import Task
from .days import Days
from django.utils import timezone
import datetime

class TaskList(ListView):
    model = Task

    def get_queryset(self):
        """Return the tasks ordered by most current"""
        return Task.objects.order_by('date_due')

    def get_context_data(self, **kwargs):
        now = timezone.now()
        context = super(TaskList, self).get_context_data(**kwargs)
        context['now'] = now.date()
        context['nowplusseven'] = (now + datetime.timedelta(days=7)).date()
        context['today'] = EachDay().today
        context['daytwo'] = EachDay().daytwo
        context['daythree'] = EachDay().daythree
        context['dayfour'] = EachDay().dayfour
        context['dayfive'] = EachDay().dayfive
        context['daysix'] = EachDay().daysix
        context['dayseven'] = EachDay().dayseven

        return context

class TaskCreate(CreateView):
    model = Task
    success_url = reverse_lazy('task_list')
    fields = ['task_type', 'person_in_charge', 'date_due']


class TaskUpdate(UpdateView):
    model = Task
    success_url = reverse_lazy('task_list')
    fields = ['task_type', 'person_in_charge', 'date_due']

class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')



class EachDay():

    def __init__(self):

        self.current_month = Days.now.strftime("%B")

        self.today = Days.now.strftime("%A")

        self.daytwo = Days.two.strftime("%A")

        self.daythree = Days.three.strftime("%A")

        self.dayfour = Days.four.strftime("%A")

        self.dayfive = Days.five.strftime("%A")

        self.daysix = Days.six.strftime("%A")

        self.dayseven = Days.seven.strftime("%A")


#testing sending service:
#could use mail_admins later instead maybe to send to everyone.
#ctx is context

def send_email(request):
    subject = "Test Subject"
    to = ['kathleen@eatwith.com']
    from_email = 'eatwith@eatwith.com'

    ctx = {'task': 'task_list'}

    #todo: write for: task_list = str(Task.objects.order_by('-date_due')[:6])
    message = loader.get_template('tasks/email/email.html').render(Context(ctx))
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()

    return HttpResponse('email sent!')

