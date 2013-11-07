# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from captures.forms import IncommingForm

def get_data(request):
    if request.method == "GET":
        form = IncommingForm()
        return render_to_response("index.html", {"form": form},
                                  context_instance=RequestContext(request))
    elif request.method == "POST":
        form = IncommingForm(data=request.POST.copy())
        if form.is_valid():
            form.save()
        return redirect("get-data")
