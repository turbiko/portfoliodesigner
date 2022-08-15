from django.db import models
from django.utils.translation import activate, gettext_lazy as _
from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index

class ProjectPage(Page):
    date = models.DateField( blank=True)
    about_project = RichTextField(blank=True)
    client = models.CharField( max_length=250, blank=True)
    tags = models.CharField(max_length=100, blank=True)
    categories = models.CharField(max_length=100, blank=True)
    pic1 = models.FileField(upload_to='pictures/', blank=True)
    pic2 = models.FileField(upload_to='pictures/', blank=True)
    pic3 = models.FileField(upload_to='pictures/', blank=True)

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

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('about_project'),
        FieldPanel('client'),
        FieldPanel('tags'),
        FieldPanel('categories'),
        FieldPanel('pic1'),
        FieldPanel('pic2'),
        FieldPanel('pic3'),
        InlinePanel('gallery_images', label="gallery images"),
    ]


class ProjectPageGalleryImage(Orderable):
    page = ParentalKey(ProjectPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]
