from django.urls import path
from catalog import views
from catalog.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5], # :5 limits results to 5 most recent
    context_object_name="message_list",
    template_name="catalog/home.html",
)

# Pointing the default path to the 'home' view in views.py
urlpatterns = [
    path("catalog/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
    path("", views.item_list, name="item_list"),
]