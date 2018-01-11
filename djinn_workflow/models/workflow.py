from django.db import models
from django.utils.translation import ugettext_lazy as _


class Workflow(models.Model):

    name = models.CharField(_(u"Name"), max_length=100, unique=True)
    initial_state = models.ForeignKey("State", related_name="initial_state",
                                      null=True, blank=True, on_delete=models.CASCADE)
    is_default = models.BooleanField(default=False)

    def __unicode__(self):

        return self.name

    __str__ = __unicode__

    class Meta:

        ordering = ("name", )
        app_label = "djinn_workflow"
