from django.contrib import admin
from article.models import Article, Category, StreamHighlight, ArticleImage, HighlightImage

# Register your models here.
class ArticleImagesInline(admin.TabularInline):
    model = ArticleImage
    extra = 1

class HighlightImagesInline(admin.TabularInline):
    model = HighlightImage
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	inlines = [ArticleImagesInline]

class StreamHighlightAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	inlines = [HighlightImagesInline]

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	def has_module_permission(self, request):
		return False

class HideInAdmin(admin.ModelAdmin):
	def has_module_permission(self, request):
		return False

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(StreamHighlight, StreamHighlightAdmin)
admin.site.register(ArticleImage, HideInAdmin)
admin.site.register(HighlightImage, HideInAdmin)