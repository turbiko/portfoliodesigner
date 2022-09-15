from django.db import models
from django.utils.translation import activate, gettext_lazy as _
from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index

from core import tools


class AboutPage(Page):
    max_count = 1
    caption = models.CharField(max_length=200)
    text_about = models.TextField(_('About text'), blank=True)
    pic1 = models.FileField(upload_to=tools.file_path, blank=True)
    pic2 = models.FileField(upload_to=tools.file_path, blank=True)
    pic3 = models.FileField(upload_to=tools.file_path, blank=True)
    pic4 = models.FileField(upload_to=tools.file_path, blank=True)
    pic5 = models.FileField(upload_to=tools.file_path, blank=True)
    pic6 = models.FileField(upload_to=tools.file_path, blank=True)

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
        InlinePanel('press_links', heading=_("PRESS"), label=_("PRESS link")),
        InlinePanel('award_links', heading=_("AWARDS"), label=_("AWARD link")),
        InlinePanel('collaborator_links', heading=_("COLABORATORS"), label=_("COLABORATOR link")),
    ]


class AboutPageCollaboratorRelatedLink(Orderable):
    page = ParentalKey(AboutPage, on_delete=models.CASCADE, related_name='collaborator_links')
    name = models.CharField(max_length=255)
    url = models.URLField()

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
    ]

class AboutPagePressRelatedLink(Orderable):
    page = ParentalKey(AboutPage, on_delete=models.CASCADE, related_name='press_links')
    name = models.CharField(max_length=255)
    url = models.URLField()

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
    ]

class AboutPageAwardsRelatedLink(Orderable):
    page = ParentalKey(AboutPage, on_delete=models.CASCADE, related_name='award_links')
    name = models.CharField(max_length=255)
    url = models.URLField()

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
    ]