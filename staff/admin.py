from django.contrib import admin
from staff.models import Staff, Role, SocialMedia
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext as _

User = get_user_model()

class HideInAdmin(admin.ModelAdmin):
	def has_module_permission(self, request):
		return False

class StaffAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

	def has_change_permission(self, request, obj=None):
		return request.user.is_superuser or (obj and obj.id == request.user.id)

class UserAdmin(BaseUserAdmin):
	def change_view(self, request, object_id):
		if request.user.is_superuser:
			self.fieldsets = (
				(None, {'fields': ('username', 'password')}),
				(_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
				(_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
				(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
				(_('Groups'), {'fields': ('groups',)}),
			)
		else:
			self.fieldsets = (
				(None, {'fields': ('username', 'password')}),
				(_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
				(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
			)

		return super(UserAdmin, self).change_view(request, object_id,)

	def has_change_permission(self, request, obj=None):
		return request.user.is_superuser or (obj and obj.id == request.user.id)

admin.site.register(Staff, StaffAdmin)
admin.site.register(Role, HideInAdmin)
admin.site.register(SocialMedia, HideInAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)