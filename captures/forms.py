# -*- coding: utf-8 -*-
import os
import base64
import tempfile
from django import forms
from django.core.files import File
from captures.models import Identificator, IFile

class IncommingForm(forms.ModelForm):

    class Meta:
        model = Identificator
        exclude = ('id_photo', 'id_scan')

    photo = forms.CharField(required=False, widget=forms.widgets.HiddenInput)
    scan = forms.CharField(required=False, widget=forms.widgets.HiddenInput)

    def create_file(self, b64, name):
        tempdir = tempfile.gettempdir()
        filename = os.path.join(tempdir, name)
        with open(filename, 'w') as fn:
            fn.write(base64.b64decode(b64))
        return File(open(filename, "r"))

    def clean_photo(self):
        id_photo = self.cleaned_data.get('photo', None)
        if not id_photo:
            return id_photo
        return self.create_file(id_photo, "webcam.png")

    def clean_scan(self):
        id_scan = self.cleaned_data.get('scan', None)
        if not id_scan:
            return id_scan
        return self.create_file(id_scan, "scan.png")

    def save(self):
        instance = super(IncommingForm, self).save()
        id_scan = self.cleaned_data.get("scan", None)
        id_photo = self.cleaned_data.get("photo", None)
        ifile_scan, ifile_photo = None, None
        if id_scan is not None:
            ifile_scan = IFile.objects.create(ifile=id_scan)
        if id_photo is not None:
            ifile_photo = IFile.objects.create(ifile=id_photo)
        instance.id_scan = ifile_scan
        instance.id_photo = ifile_photo
        instance.save()
