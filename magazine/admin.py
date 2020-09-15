from django.contrib import admin
from magazine.models import Magazine, Highlight

class HighlightInline(admin.TabularInline):
    model = Highlight
    extra = 3

class HighlightHideInAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

class MagazineAdmin(admin.ModelAdmin):
	exclude = ['date_published']
	prepopulated_fields = {'slug': ('headline',)}
	inlines = [HighlightInline]

admin.site.register(Magazine, MagazineAdmin)
admin.site.register(Highlight, HighlightHideInAdmin)