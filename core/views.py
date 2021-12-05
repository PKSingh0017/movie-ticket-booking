from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from django.conf import settings
import os
import mimetypes

from . import forms as core_forms
from . import models as core_models


# For mails
from django.conf import settings
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
SENDER_EMAIL = settings.EMAIL_HOST_USER
# For mails

def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid

def home(request):
    all_movies = core_models.Movie.objects.all()
    context = {
        'all_movies': all_movies
    }
    return render(request, 'core/index.html', context)