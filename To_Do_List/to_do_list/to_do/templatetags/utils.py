from django import template
import datetime
from django.utils.timezone import make_aware

register = template.Library()

def due_delta(value):
    current_time = make_aware(datetime.datetime.now())
    due_time = value

    delta = due_time - current_time
    return delta.days


register.filter('due_delta', due_delta)