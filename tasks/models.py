from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Group, User
from .days import Days
import datetime
from django.utils import timezone

class Task(models.Model):
    task_type = models.ForeignKey(Group)
    person_in_charge = models.ForeignKey(User)
    date_due = models.DateField('date due')

    def __unicode__(self):
        return self.tasktype

    def get_absolute_url(self):
        return reverse('task_edit', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.task_type

    def is_due_today(self):
        return self.date_due == datetime.datetime.now().date()

    def is_due_two(self):
        return self.date_due == Days.two.date()

    def is_due_three(self):
        return self.date_due == Days.three.date()

    def is_due_four(self):
        return self.date_due == Days.four.date()

    def is_due_five(self):
        return self.date_due == Days.five.date()

    def is_due_six(self):
        return self.date_due == Days.six.date()

    def is_due_seven(self):
        return self.date_due == Days.seven.date()

    def to_show(self):
        return self.date_due >= datetime.datetime.now().date()

    """to_show.admin_order_field = 'date_due'
    to_show.boolean = True
    to_show.short_description = 'To filter out past tasks.'"""