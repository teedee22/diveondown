""" Streamfields live in here. """

from wagtail.core import blocks


class RichTextBlock(blocks.RichTextBlock):
    """Richtext"""

    class Meta:  # noqa
        template = "streams/richtextblock.html"
        icon = "edit"
        label = "Richtext"
