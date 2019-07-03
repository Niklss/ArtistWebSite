from django.db import models
from django.utils.translation import gettext_lazy as _


class ArtManager(models.Manager):
    def add_art(self, name, year, description):
        entity = self.model(name=name, year=year, description=description)
        return entity


class Art(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField(_('year'), null=True)
    description = models.CharField(_('description'), max_length=255, null=True)
    image = models.ImageField(_('image'), upload_to='images/', null=True)
    objects = ArtManager()

    class Meta:
        verbose_name = _('Art')

    verbose_name_plural = _('Arts')

    def __int__(self):
        return self.name
