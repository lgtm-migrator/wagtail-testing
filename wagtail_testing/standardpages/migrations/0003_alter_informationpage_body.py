# Generated by Django 4.0.5 on 2022-07-02 09:11

from django.db import migrations
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("standardpages", "0002_remove_informationpagerelatedpage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="informationpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "heading",
                        wagtail.blocks.CharBlock(
                            form_classname="full title",
                            icon="title",
                            template="streamfield/blocks/heading_block.html",
                        ),
                    ),
                    ("paragraph", wagtail.blocks.RichTextBlock()),
                    (
                        "image",
                        wagtail.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                ("caption", wagtail.blocks.CharBlock(required=False)),
                            ]
                        ),
                    ),
                    (
                        "quote",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "quote",
                                    wagtail.blocks.CharBlock(form_classname="title"),
                                ),
                                (
                                    "attribution",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                            ]
                        ),
                    ),
                    ("embed", wagtail.embeds.blocks.EmbedBlock()),
                    (
                        "call_to_action",
                        wagtail.snippets.blocks.SnippetChooserBlock(
                            "utils.CallToActionSnippet",
                            template="streamfield/blocks/call_to_action_block.html",
                        ),
                    ),
                    (
                        "document",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "document",
                                    wagtail.documents.blocks.DocumentChooserBlock(),
                                ),
                                ("title", wagtail.blocks.CharBlock(required=False)),
                            ]
                        ),
                    ),
                ],
                use_json_field=None,
            ),
        ),
    ]
