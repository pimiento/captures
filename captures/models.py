# -*- coding: utf-8 -*-
import os
import time
import hashlib
import datetime
import mimetypes
from django.db import models
from django.conf import settings

class Identificator(models.Model):

    class Meta:
        db_table = 'identificator'
        app_label = 'captures'

    first_name = models.CharField(max_length=128, verbose_name=u'Имя')
    middle_name = models.CharField(max_length=256, verbose_name=u'Отчество')
    last_name = models.CharField(max_length=256, verbose_name=u'Фамилия')
    id_photo = models.ForeignKey('captures.IFile', null=True, related_name=u'photo')
    id_scan = models.ForeignKey('captures.IFile', null=True, related_name=u'scan')

class IFile(models.Model):

    class Meta:
        db_table = 'ifile'
        app_label = 'captures'

    def file_upload_to(instance, filename):
        timestamp = time.mktime(datetime.datetime.now().timetuple())
        return "%s/%s" % (timestamp, os.path.basename(filename))

    created = models.DateTimeField(auto_now_add=True)
    filename = models.CharField(max_length=100, editable=False)
    ifile = models.FileField(upload_to=file_upload_to, max_length=1024)

    def save(self, *args, **kwargs):
        file_basename = os.path.basename(self.ifile.name)
        self.filename = file_basename
        super(IFile, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        path = self.ifile.path
        try:
            os.unlink(path)
        except OSError:
            pass
        finally:
            super(IFile, self).delete()
