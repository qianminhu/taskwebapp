from django.test import TestCase
from .models import Task
from django.utils import timezone
import datetime
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

"""
test models and views:
-internal behavior of the code.
-behavior as it would be experienced by a user through a web browser.
"""


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        :return:
        """
        self.assertEqual(1 + 1, 2)

class TaskMethodTests(TestCase):

    def test_due_date_in_past(self):
        """
        to_show() should return False for questions with due_date in past
        """
        time = timezone.now() - datetime.timedelta(days=1)
        past_task = Task(date_due = time.date())
        self.assertEqual(past_task.to_show(), False)


    def test_due_date_in_future(self):
        """
        to_show() should return True for questions with due_date in future
        :return:
        """
        time = timezone.now() + datetime.timedelta(days=5)
        future_task = Task(date_due = time.date())
        self.assertEqual(future_task.to_show(), True)

    def test_due_date_today(self):
        """
        to_show() should return True for questions with due_date of today's date
        :return:
        """
        time = timezone.now()
        today_task = Task(date_due = time.date())
        self.assertEqual(today_task.to_show(), True)


def create_task(days, task_type, person_in_charge): #todo: why doesn't task_type or person_in_charge show??
    time = timezone.now() + datetime.timedelta(days=days)
    task_type=Group.objects.order_by('?').first()
    person_in_charge=User.objects.order_by('?').first()
    return Task.objects.create(date_due=time, task_type=task_type, person_in_charge=person_in_charge)


class ListViewTests(TestCase):
    fixtures = ['tasks_testdata.json']

    def test_list_with_no_tasks(self):
        """
        if no tasks, message should be displayed
        :return:
        """
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No tasks due!")
        self.assertQuerysetEqual(response.context['object_list'], [])


    #todo: fix this test
    def test_list_with_past_tasks(self):
        """
        if list has tasks with date_due in the past, they should not be displayed
        :return:
        """
        create_task(-20,task_type=Group.objects.order_by('?').first(), person_in_charge=User.objects.order_by('?').first())
        response = self.client.get(reverse('task_list'))
        self.assertQuerysetEqual(
            response.context['object_list'], []
        )

    def test_list_with_future_tasks(self):
        """
        if list has tasks with date_due in the future, they should be displayed
        :return:
        """
        pass

    def test_list_with_past_and_future(self):
        """
        only future tasks should be displayed if both past and future tasks exist
        :return:
        """
        pass


    def test_list_can_display_multiple(self):
        """
        the list view should be able to display multiple tasks
        :return:
        """
        pass


#todo: other test ideas: if there is no (ex: date_due, person_in_charge, task_type), task should not be published.


#also can test that each day of the calendar matches the right date and then each task under it matches the date it should correspond to
class CalViewTests(TestCase):
    pass