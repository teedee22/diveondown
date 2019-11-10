from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField


class AboutPage(Page):
    template = "about/about_page.html"
    max_count = 1
    banner_title_1 = models.CharField(max_length=50, blank=True, null=True)
    banner_title_2 = models.CharField(max_length=50, blank=True, null=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    about_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    about_title = models.CharField(max_length=100, blank=True, null=True)
    about_text = RichTextField(
        features=["bold", "italic"], blank=True, null=True
    )
    reddit_url = models.URLField(blank=True, null=True, help_text="Reddit URL")
    instagram_url = models.URLField(blank=True, null=True, help_text="Instagram URL")
    youtube_url = models.URLField(blank=True, null=True, help_text="Youtube URL")
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("banner_title_1"),
                FieldPanel("banner_title_2"),
                ImageChooserPanel("banner_image"),
            ],
            heading="Banner Options",),
        MultiFieldPanel(
            [
                ImageChooserPanel("about_image"),
                FieldPanel("about_title"),
                FieldPanel("about_text"),
                FieldPanel("instagram_url"),
                FieldPanel("reddit_url"),
                FieldPanel("youtube_url"),
            ]
        )

    ]
