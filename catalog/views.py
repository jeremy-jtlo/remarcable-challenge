import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from catalog.forms import LogMessageForm
from catalog.models import LogMessage
from catalog.models import Item, Category, Tag
from django.db.models import Q
from django.views.generic import ListView

# Create your views here.

## Leftover from MS tutorial
def home(request):
    return render(request, "catalog/home.html")

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, "catalog/about.html")

def contact(request):
    return render(request, "catalog/contact.html")

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
        
    else:
        return render(request, "catalog/log_message.html", {"form": form})

def hello_there(request, name):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'catalog/catalog.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

# View for products and items
def item_list(request):
    query = request.GET.get('q') # Our search string
    category_id = request.GET.get('category') # Result of the dropdown
    tag_ids = request.GET.getlist('tag') # Ctrl+Click selected tag(s)

    # Fetch everything in the DB
    items = Item.objects.all()

    # Filtering process: because we can combine search and filter logic,
    # don't use elif.
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    if category_id:
        items = items.filter(category_id=category_id)

    if tag_ids:
        items = items.filter(tags__id__in=tag_ids).distinct()


    categories = Category.objects.all()
    tags = Tag.objects.all()

    # Template needs to render the filtered item list, all categories, etc
    context = {
        'items': items,
        'categories': categories,
        'tags': tags,
        'query': query,
        'selected_category': category_id,
        'selected_tag': tag_ids,
    }
    return render(request, 'catalog/item_list.html', context)