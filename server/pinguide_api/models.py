from django.db import models


class ImageManager(models.Manager):
    pass


class Image(models.Model):
    objects = ImageManager()
    url = models.CharField(max_length=256)

    def __unicode__(self):
        return '{} {}'.format(self.id, self.url)

    def as_json(self):
        return dict(
            id=self.id,
            url=self.url,
        )