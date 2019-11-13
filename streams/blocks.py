""" Streamfields live in here. """

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class RichTextBlock(blocks.RichTextBlock):
    """Richtext"""

    class Meta:  # noqa
        template = "streams/richtextblock.html"
        icon = "edit"
        label = "Richtext"


class SingleImageBlockLarge(blocks.StructBlock):
    """ Small Image """
    image = ImageChooserBlock(required=True)
    caption = blocks.CharBlock(required=False, null=True, max_length=250)

    class Meta:
        template = "streams/single_image_block_large.html"
        icon = "image"
        label = "Large Image"


class SingleImageBlockSmall(blocks.StructBlock):
    """ Large Image"""
    image = ImageChooserBlock(required=True)
    caption = blocks.CharBlock(required=False, null=True, max_length=250)

    class Meta:
        template = "streams/single_image_block_small.html"
        icon = "image"
        label = "Small Image"


class YouTubeEmbedBlock(blocks.StructBlock):
    """Youtube embed"""
    embed_url = blocks.URLBlock(blank=True, null=False)

    class Meta:
        template = "streams/youtube_embed_block.html"
        icon = "media"
        label = "youtube embed"
