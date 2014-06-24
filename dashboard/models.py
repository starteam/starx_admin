from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
from django.contrib import admin

# Create your models here.
class Product(TimeStampedModel):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title
    pass

admin.site.register(Product)

class PublicURL(TimeStampedModel):
    title = models.CharField(max_length=60)
    note = models.TextField()
    url = models.URLField()
    current_cc = models.ForeignKey('PublicURL')
    def __str__(self):
        return self.title
    pass

admin.site.register(PublicURL)

class CompiledConfig(TimeStampedModel):
    data = models.TextField(max_length=1024*1024)
    public_url = models.ForeignKey(PublicURL)

    def save(self, *args, **kwargs):
        if self.public_url is None:
            super(Config,self).save(*args,**kwargs);
        else:
            raise Exception("CompiledConfig can not be changed once published.")
    pass

admin.site.register(CompiledConfig)

class Config(TimeStampedModel):
    title = models.CharField(max_length=60)
    note = models.TextField()
    owner = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    compiled = models.ForeignKey(CompiledConfig, null=True)
    data = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True)

    def save(self, *args,**kwargs):
        if self.compiled is None:
            super(Config,self).save(*args,**kwargs);
        else:
            raise Exception("Config can not be changed once published.")

admin.site.register(Config)

class AuditLog(TimeStampedModel):
    user = models.ForeignKey(User)
    action = models.CharField(max_length=60)
    details = models.TextField()

admin.site.register(AuditLog)
