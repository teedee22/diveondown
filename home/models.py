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
    banner_subtitle = models.CharField(max_length=50, blank=True, null=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    featured_blog_post = models.ForeignKey(
        "wagtailcore.page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    content_panels = Page.content_panels + [
    MultiFieldPanel(
        [
            FieldPanel("banner_subtitle"),
            ImageChooserPanel("banner_image"),
        ],
        heading="Banner Options",

    ),
    PageChooserPanel("featured_blog_post"),]
