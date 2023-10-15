from django.shortcuts import render
from . import models


def postView(request):
    post_value = models.Post.objects.all()
    context =

