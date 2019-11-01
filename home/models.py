from django.db import models
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    PageChooserPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page


class HomePage(Page):
    template="home/home_page.html"
    max_count = 1
    banner_title_1 = models.CharField(max_length=50, blank=True, null=True)
    banner_title_2 = models.CharField(max_length=50, blank=True, null=True)
    banner_title_3 = models.CharField(max_length=50, blank=True, null=True)
    banner_title_4 = models.CharField(max_length=50, blank=True, null=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    content_panels = Page.content_panels + [
    MultiFieldPanel(
        [
            FieldPanel("banner_title_1"),
            FieldPanel("banner_title_2"),
            FieldPanel("banner_title_3"),
            FieldPanel("banner_title_4"),
            ImageChooserPanel("banner_image"),
        ],
        heading="Banner Options",
    ),]
