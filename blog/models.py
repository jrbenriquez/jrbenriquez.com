from django import forms
from django.db import models
from django.db.models.query import QuerySet

from modelcluster.models import ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.snippets.models import register_snippet
from wagtail.fields import StreamField
from wagtail.models import Page, ParentalKey
from wagtail.models import Orderable
from wagtail import blocks
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index
from wagtailcodeblock.blocks import CodeBlock
from wagtail.images.blocks import ImageBlock


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        context = super().get_context(request)
        children = self.get_children().live().order_by("-first_published_at")
        context["blogpages"] = children
        return context

    content_panels = Page.content_panels + [FieldPanel("intro")]


class BlogPostTag(TaggedItemBase):
    content_object = ParentalKey(
        "BlogPostPage", related_name="tagged_items", on_delete=models.CASCADE
    )


class BlogPostPage(Page):
    gallery_images: QuerySet

    POST_TYPE_CHOICES = [
        ("blog", "Blog Post"),
        ("explainer", "Explainer"),
    ]

    post_type = models.CharField(
        max_length=20,
        choices=POST_TYPE_CHOICES,
        default="blog",
        help_text="Type of post",
    )
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    content = StreamField(
        [
            ("heading", blocks.CharBlock(form_classname="title")),
            ("paragraph", blocks.RichTextBlock()),
            ("image", ImageBlock()),
            ("code", CodeBlock(label="Code Block")),
            ("raw_html", blocks.RawHTMLBlock(label="Raw HTML")),
        ],
        use_json_field=True,
        null=True,
        blank=True,
    )

    authors = ParentalManyToManyField("blog.Author", blank=True)

    tags = ClusterTaggableManager(through=BlogPostTag)

    def main_image(self):
        record = self.gallery_images.first()
        if record:
            return record.image
        return None

    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("content"),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("post_type"),
                FieldPanel("date"),
                FieldPanel("authors", widget=forms.CheckboxSelectMultiple),
                FieldPanel("tags"),
            ],
            heading="Blog information",
        ),
        FieldPanel("intro"),
        FieldPanel("content"),
        InlinePanel("gallery_images", label="Gallery images"),
    ]


class BlogPostGalleryImage(Orderable):
    page = ParentalKey(
        BlogPostPage, on_delete=models.CASCADE, related_name="gallery_images"
    )
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    caption = models.CharField(max_length=250, blank=True)

    panels = [
        FieldPanel("image"),
        FieldPanel("caption"),
    ]


@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    author_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("email"),
        FieldPanel("author_image"),
    ]

    def __str__(self):
        return self.name


class BlogTagPage(Page):
    def get_context(self, request):
        tag = request.GET.get("tag")
        blogpages = BlogPostPage.objects.filter(tags__name=tag)
        context = super().get_context(request)
        context["blogpages"] = blogpages
        return context


# Specialized Index Pages for filtering by post type
class BlogOnlyIndexPage(Page):
    """Index page that shows only Blog Posts"""

    intro = RichTextField(blank=True)

    def get_context(self, request):
        context = super().get_context(request)
        children = (
            BlogPostPage.objects.live()
            .filter(post_type="blog")
            .order_by("-first_published_at")
        )
        context["blogpages"] = children
        return context

    content_panels = Page.content_panels + [FieldPanel("intro")]

    class Meta:
        verbose_name = "Blog Post Index Page"


class ExplainerIndexPage(Page):
    """Index page that shows only Explainers"""

    intro = RichTextField(blank=True)

    def get_context(self, request):
        context = super().get_context(request)
        children = (
            BlogPostPage.objects.live()
            .filter(post_type="explainer")
            .order_by("-first_published_at")
        )
        context["blogpages"] = children
        return context

    content_panels = Page.content_panels + [FieldPanel("intro")]

    class Meta:
        verbose_name = "Explainer Index Page"
