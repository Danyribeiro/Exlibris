
from django.views.generic import (
     ListView,  
     CreateView,
     UpdateView,
     DeleteView
                          
                                
)
from .models import Book
from .forms import  BookForm
from django.urls import reverse
from django.shortcuts import get_object_or_404



# Create your views here.
class CatalogListView(ListView):
    paginate_by=3
    template_name="catalog/catalog_list.html"
    model = Book
    
    def get_queryset(self):
            name = self.request.GET.get("name")
            if name:
                object_list = self.model.objects.filter(title_icontains=name)
            else:
                object_list = self.model.objects.all()
            return object_list

   
class CatalogCreateView(CreateView):
    template_name="catalog/catalog.html"
    form_class = BookForm

    def form_valid(self, form):
        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse("catalog:catalog-list")
    
class CatalogUpdateView(UpdateView):
        template_name = "catalog/catalog.html"
        form_class = BookForm 

        def get_object(self):
            id = self.kwargs.get("id")
            return get_object_or_404(Book, id=id)


        def form_valid(self, form):
            return super().form_valid(form)
        
        def get_success_url(self):
            return reverse("catalog:catalog-list")
        
class CatalogDeleteView(DeleteView):
        def get_object(self):
            id = self.kwargs.get("id")
            return get_object_or_404(Book, id=id)
        def get_success_url(self):
            return reverse("catalog:catalog-list")

       
        
        

