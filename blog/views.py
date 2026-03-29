from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.template.response import TemplateResponse
from blog.models import BlogPostPage

def search(request):
    query = request.GET.get("query")
    page = request.GET.get("page", 1)

    # Filter by post type based on referrer URL
    base_queryset = BlogPostPage.objects.live()
    referrer = request.META.get("HTTP_REFERER", "")

    if "explainer" in referrer.lower():
        base_queryset = base_queryset.filter(post_type="explainer")
    elif "blog" in referrer.lower():
        base_queryset = base_queryset.filter(post_type="blog")
    # If home page or other, show all posts (no filter)

    if query:
        search_results = base_queryset.search(query)
    else:
        search_results = base_queryset

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    context = {"blogpages": search_results}

    return TemplateResponse(request, "blog/partials/blog_page_list.html", context)
