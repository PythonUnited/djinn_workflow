from django.db import models
from django.contrib.auth.models import Permission
from django.utils.translation import ugettext_lazy as _


class Transition(models.Model):

    name = models.CharField(_(u"Name"), max_length=100)
    destination = models.ForeignKey(
        "State",
        verbose_name=_(u"Destination"),
        related_name="destination_state",
        on_delete=models.CASCADE)
    permission = models.ForeignKey(
        Permission,
        verbose_name=_(u"Permission"), blank=True, null=True,
        on_delete=models.CASCADE)
    state = models.ForeignKey("State", on_delete=models.CASCADE)

    def __unicode__(self):

        return self.name

    __str__ = __unicode__

    class Meta:

        ordering = ("name", )
        app_label = "djinn_workflow"
