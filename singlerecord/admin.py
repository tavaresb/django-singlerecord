from django.contrib import admin
from django.shortcuts import redirect

class SingleRecordModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        """ Prevent addition of new objects """
        return False

    def changelist_view(self, request, extra_context=None):
        """ 
        Prevent object list, go to edition of the 
         single record in database
        """
        info = self.model._meta.app_label, self.model._meta.module_name
        return redirect('admin:%s_%s_change' % info, 1)
        
    def change_view(self, request, object_id, extra_context=None):
        if object_id != '1':
            info = self.model._meta.app_label, self.model._meta.module_name
            return redirect('admin:%s_%s_change' % info, 1)

        # Make sure we have the object in the database
        self.model.objects.get_or_create(pk=1)

        return super(SingleRecordModelAdmin, self).change_view(
            request,
            object_id,
            extra_context=extra_context,
        )
