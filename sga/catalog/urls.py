from django.urls import path
from .views import (
    CatalogListView,
    CatalogCreateView,
    CatalogUpdateView,
    CatalogDeleteView,
)

app_name = "catalog"
urlpatterns = [
    path("list/", CatalogListView.as_view(), name="catalog-list"),
    path("", CatalogCreateView.as_view(), name="catalog-create"),
    path("<int:id>/", CatalogUpdateView.as_view(), name="catalog-update"),
    path("<int:id>/delete/", CatalogDeleteView.as_view(), name="catalog-delete"),
]
