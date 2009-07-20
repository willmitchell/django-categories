from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from categories.models import Category
from stories.models import Story
from django.db.models import Q
from django.views.decorators.cache import cache_page

def category_detail(request, slug, with_stories=False, 
    template_name='categories/category_detail.html'):
    context = {}
    category = get_object_or_404(Category,
        slug__iexact=slug)
        
    context['category'] = category
    
    if with_stories:
        stories = Story.published.filter(Q(primary_category=category) | Q(categories__in=[category,]))
        context['stories'] = stories
        
    return render_to_response(template_name,
        context,
        context_instance=RequestContext(request)
    )
