from django.urls import path

from . import views

urlpatterns = [
    path("", views.all_posts, name="all-posts"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page"),
    path("read-later/", views.read_later_view, name="read-later-page"),
    path("add-to-read-later/<slug:slug>", views.add_to_read_later, name="add-to-read-later"),
    path("remove-from-read-later/<slug:slug>", views.remove_from_read_later, name="remove-from-read-later"),
]
