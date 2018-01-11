from django.db import models
from django.contrib.contenttypes.models import ContentType
from djinn_workflow.models.workflow import Workflow


class ModelWorkflow(models.Model):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)

    def __unicode__(self):
        return "%s - %s" % (self.content_type.name, self.workflow.name)

    __str__ = __unicode__

    class Meta:

        app_label = "djinn_contenttypes"
