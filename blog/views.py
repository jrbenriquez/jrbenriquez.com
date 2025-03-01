from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.template.response import TemplateResponse
from blog.models import BlogPostPage

def search(request):
    query = request.GET.get("query")
    page = request.GET.get("page", 1)
    if query:
        search_results = BlogPostPage.objects.live().search(query)
    else:
        search_results = BlogPostPage.objects.live()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    context = {
        "blogpages": search_results
    }

    return TemplateResponse(request, "blog/partials/blog_page_list.html", context )


