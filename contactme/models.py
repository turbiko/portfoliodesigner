from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.models import Page, Orderable
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)
from core import tools

class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class ContactPage(Page):
    max_count = 1
    template = "contactme/contact_page.html"
    # This is the default path.
    # If ignored, Wagtail adds _landing.html to your template name
    landing_page_template = "contactme/contact_page_landing.html"

    pic1 = models.FileField(upload_to=tools.file_path, blank=True)
    pic2 = models.FileField(upload_to=tools.file_path, blank=True)
    intro = RichTextField(blank=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    to_email = models.EmailField(blank=True)
    from_email = models.EmailField(blank=True)
    subject = models.CharField(max_length=150, blank=True)
    google_address = models.URLField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('pic1'),
        FieldPanel('pic2'),
        MultiFieldPanel([
            FieldPanel('address'),
            FieldPanel('phone'),
            FieldRowPanel([
                FieldPanel('from_email', classname="col6"),
                FieldPanel('to_email', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Contact Settings"),
        FieldPanel('google_address'),
    ]