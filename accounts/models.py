from django.conf import settings
from django.db import models
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    about = models.CharField(max_length=120, null=True, blank=True)
    cash = models.PositiveIntegerField(default=1000)
    health = models.PositiveIntegerField(default=10)
    mana = models.PositiveIntegerField(default=30)

    def __str__(self):
        return str(self.user.username)

    def __unicode__(self):
        return str(self.user.username)


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass


post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)
