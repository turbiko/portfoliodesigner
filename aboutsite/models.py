from django.db import models
from django.utils.translation import activate, gettext_lazy as _
from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index

class AboutPage(Page):
    caption = models.CharField(max_length=200)
    text_about = models.TextField(_('About text'), blank=True)
    pic1 = models.FileField(upload_to='pictures/', blank=True)
    pic2 = models.FileField(upload_to='pictures/', blank=True)
    pic3 = models.FileField(upload_to='pictures/', blank=True)
    pic4 = models.FileField(upload_to='pictures/', blank=True)
    pic5 = models.FileField(upload_to='pictures/', blank=True)
    pic6 = models.FileField(upload_to='pictures/', blank=True)

    class Meta:
        verbose_name = "About Page"

    def get_project(self):
        return self

    content_panels = Page.content_panels + [
        FieldPanel('caption'),
        FieldPanel('text_about'),
        FieldPanel('pic1'),
        FieldPanel('pic2'),
        FieldPanel('pic3'),
        FieldPanel('pic4'),
        FieldPanel('pic5'),
        FieldPanel('pic6'),

    ]
