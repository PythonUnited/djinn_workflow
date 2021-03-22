from django.contrib import admin
from djinn_workflow.models import ObjectState, Workflow, ModelWorkflow, \
    Transition, PermissionAssignment, State


class ModelWorkflowAdmin(admin.ModelAdmin):
    pass


class ObjectStateAdmin(admin.ModelAdmin):
    list_filter = ['object_ct', 'state']


class PermissionAssignmentAdmin(admin.ModelAdmin):
    pass


class StateAdmin(admin.ModelAdmin):
    pass


class TransitionAdmin(admin.ModelAdmin):
    pass


class WorkflowAdmin(admin.ModelAdmin):
    pass


admin.site.register(ModelWorkflow, ModelWorkflowAdmin)
admin.site.register(ObjectState, ObjectStateAdmin)
admin.site.register(PermissionAssignment, PermissionAssignmentAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Transition, TransitionAdmin)
admin.site.register(Workflow, WorkflowAdmin)
