from django.db import models
from django.core.paginator import Paginator

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from blog.models import BlogIndexPage


class HomePage(Page):
    self_photo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="This is me!",
    )

    self_text = models.CharField(
        blank=True, max_length=255, help_text="Write an introduction for the site"
    )

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )

    hero_text = models.CharField(
        blank=True, max_length=255, help_text="Write an introduction for the site"
    )
    hero_cta = models.CharField(
        blank=True,
        verbose_name="Hero CTA",
        max_length=255,
        help_text="Text to display on Call to Action",
    )
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero CTA link",
        help_text="Choose a page to link to for the Call to Action",
    )
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("self_photo"),
                FieldPanel("self_text"),
                # FieldPanel("hero_text"),
                # FieldPanel("hero_cta"),
                # FieldPanel("hero_cta_link"),
            ],
            heading="Main Section",
        ),
        FieldPanel("body"),
    ]

    def get_context(self, request):
        # Provides the 10 most recent Blog Posts (all types)
        context = super().get_context(request)
        from blog.models import BlogPostPage

        # Get all BlogPostPages regardless of parent, ordered by date
        children = BlogPostPage.objects.live().order_by("-first_published_at")

        paginator = Paginator(children, 10)
        blogpages = paginator.page(1)
        context["blogpages"] = blogpages
        return context
