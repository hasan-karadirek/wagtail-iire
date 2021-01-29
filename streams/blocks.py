from wagtail.core import blocks
from django.db import models
from wagtailmodelchooser.blocks import ModelChooserBlock


class ServiceFeaturesImgRBlock(blocks.StructBlock):
    service=ModelChooserBlock('services.Services')

    class Meta:
        template="streams/service_features_right_image.html"
        icon="edit"
        label="Service Features Image Right"
class ServiceFeaturesImgLBlock(blocks.StructBlock):
    service=ModelChooserBlock('services.Services')

    class Meta:
        template="streams/service_features_left_image.html"
        icon="edit"
        label="Service Features Image Left"
class RichTextBlock(blocks.RichTextBlock):
    class Meta:
        template="streams/rich_text.html"
        icon="edit"
        label="Rich Text Field"