from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):

        main_tags = [form.cleaned_data.get('is_main') for form in self.forms if form.cleaned_data]

        if main_tags.count(True) > 1:
            raise ValidationError('Основным может быть только один тег.')

        if not any(main_tags):
            raise ValidationError('Укажите основной тег.')

        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    search_fields = ('title',)
    list_filter = ('published_at',)

    inlines = [RelationshipInline]
