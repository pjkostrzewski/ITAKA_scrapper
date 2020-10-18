from __future__ import absolute_import, unicode_literals

from celery import shared_task
import time


@shared_task
def send_email(email, message):
    """
    easy function to understand how celery works
    :param email:
    :param message:
    :return:
    """
    time.sleep(12)
    print("Email sent to {}. Message sent was - '{}'".format(email, message))
