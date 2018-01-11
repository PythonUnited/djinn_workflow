from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from djinn_workflow.models.state import State


class ObjectState(models.Model):

    object_ct = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('object_ct', 'object_id')
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __unicode__(self):
        return "%s - %s" % (self.content_object, self.state)

    __str__ = __unicode__

    class Meta:
        app_label = "djinn_workflow"
        unique_together = ("object_ct", "object_id")
