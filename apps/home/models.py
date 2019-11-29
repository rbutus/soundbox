from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField

from apps.streams import blocks


class HomePage(Page):

    content = StreamField(
        [
            ('title_and_text', blocks.TitleAndTextBlock(name='title_and_text'))
        ],
        null=True,
        blank=True,

    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = "Homepage"
        verbose_name_plural = "Homepage"

