import re
import subprocess

from django.http import HttpResponse


def log(request, severity):
    notification = get_notification(request)
    if severity == 'fatal':
        subprocess.check_output(['notify-send', notification])
    print(severity, '::', notification)
    return HttpResponse('OK', content_type="text/plain")


### PRIVATE ###

def clean(text):
    return re.sub(r'[^a-zA-Z0-9\._\-]', '', text)


def trim(text):
    return text[:128]


def get_notification(request):
    notification_dirty = request.body.decode()
    notification_clean = clean(notification_dirty)
    notification = trim(notification_clean)
    return notification
