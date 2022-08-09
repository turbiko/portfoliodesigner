import uuid
import os

from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _

from wagtail.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    StreamFieldPanel,
    PageChooserPanel,
    ObjectList,
    TabbedInterface,
)
# Create your models here.


COMPANY_PATH = 'company'

def get_logo_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'logo-{uuid.uuid4()}.{ext}'
    print(instance)
    return os.path.join(COMPANY_PATH+'/logo', filename)


class Company(Page):
    name = models.CharField(_(''), max_length=250)
    regnum = models.CharField(_(''), max_length=20)
    description =  RichTextField(_("About company text"), null=True, blank=True,)
    logo = models.ImageField(
        _(''),
        null=True,
        blank=True,
        upload_to=get_logo_upload_path,
        default=COMPANY_PATH+'/user-default.png',
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])]
    )

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('regnum'),
        FieldPanel('description'),
        FieldPanel('logo'),
    ]



