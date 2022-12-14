from django.db import models
from django import forms

from django.utils.translation import activate, gettext_lazy as _
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from taggit.models import TaggedItemBase
from wagtail.snippets.models import register_snippet

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index
from core import tools

@register_snippet
class ProjectCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Project categories'


class ProjectPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ProjectPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class ProjectPage(Page):
    date = models.DateField( blank=True)
    about_project = RichTextField(blank=True)
    client = models.CharField( max_length=250, blank=True)
    # tags = models.CharField(max_length=100, blank=True)
    tags = ClusterTaggableManager(through=ProjectPageTag, blank=True)
    categories = ParentalManyToManyField('ProjectCategory', blank=True)
    project_teaser = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL,  related_name='+', null=True
    )
    file = models.FileField(
        upload_to=tools.file_path, blank=True)  # TODO: upload_to method need to know project and folder name for create dirs

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('about_project'),
        FieldPanel('client'),
        FieldPanel("tags"),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        FieldPanel('project_teaser'),
        InlinePanel('gallery_images', label="Portfolio images"),
    ]

    class Meta:
        verbose_name = "Project Page"

    search_fields = Page.search_fields + [
        index.SearchField('client'),
        index.SearchField('about_project'),
        index.SearchField('tags'),
        index.SearchField('categories'),
    ]

    def get_project(self):
        return self




class ProjectPageGalleryImage(Orderable):
    page = ParentalKey(ProjectPage, on_delete=models.CASCADE, related_name='gallery_images', null=True, default=None)
    file = models.FileField(
            upload_to=tools.file_path, blank=True)  # TODO: upload_to method need to know project and folder name for create dirs
    name = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('name'),
        FieldPanel('file'),
    ]

