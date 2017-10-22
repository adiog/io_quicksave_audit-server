import re
import subprocess

from django.http import HttpResponse


def clean(text):
    return re.sub(r'[^a-zA-Z0-9\._\-]', '', text)


def log(request, severity):
    notification_dirty = request.body.decode()
    notification = clean(notification_dirty)
    if severity == 'fatal':
        subprocess.check_output(['notify-send', notification])
    print(severity, '::', notification)
    return HttpResponse('OK', content_type="text/plain")
