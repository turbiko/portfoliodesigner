from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import MultiFieldPanel, FieldPanel
from wagtail.models import Page

from project.models import ProjectPage

class HomePage(Page):
    facebook_url = models.URLField(_('facebook'), max_length=200, null=True, blank=True)
    youtube_url = models.URLField(_('youtube'), max_length=200, null=True, blank=True)
    twitter_url = models.URLField(_('twitter'), max_length=200, null=True, blank=True)
    instagram_url = models.URLField(_('instagram'), max_length=200, null=True, blank=True)

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['project_pages'] = ProjectPage.objects.child_of(self).live()
        return context

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('facebook_url'),
            FieldPanel('youtube_url'),
            FieldPanel('twitter_url'),
            FieldPanel('instagram_url'),
        ], heading="Social Links"),
    ]