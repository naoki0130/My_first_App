from django.urls import path
from . import views

urlpatterns = [
    path("features/", views.features, name="features"),
    path("about/", views.about, name="about"),
    path("faq/", views.faq, name="faq"),
    path("portfolio/", views.portfolio, name="portfolio"),
]