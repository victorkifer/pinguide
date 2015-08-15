from django.db import models


class ImageManager(models.Manager):
    pass


class Image(models.Model):
    objects = ImageManager()
    img_id = models.IntegerField()
    url = models.CharField(max_length=250)

    def __unicode__(self):
        return '{} {}'.format(self.img_id, self.url)

    def as_json(self):
        return dict(
            id=self.id,
            img_id=self.img_id,
            url=self.url,
        )