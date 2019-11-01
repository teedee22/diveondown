from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel

# Create your models here.


@register_setting
class SocialMediaAndLogoSettings(BaseSetting):
    """Social media settings for our custom website"""

    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    site_name = models.CharField(max_length=50, blank=True, null=True)
    facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter URL")
    youtube = models.URLField(
        blank=True, null=True, help_text="Youtube Channel URL"
    )
    reddit = models.URLField(
        blank=True, null=True, help_text="Reddit Channel URL"
    )
    instagram = models.URLField(
        blank=True, null=True, help_text="Gram Channel URL"
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("site_name"),
                ImageChooserPanel("logo"),
                FieldPanel("facebook"),
                FieldPanel("twitter"),
                FieldPanel("youtube"),
                FieldPanel("reddit"),
                FieldPanel("instagram"),
            ],
            heading="Navbar social media, logo and site name settings",
        )
    ]
