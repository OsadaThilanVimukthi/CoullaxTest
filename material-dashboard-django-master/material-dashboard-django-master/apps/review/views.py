from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from apps.review.models import BookReview
from apps.review.serializers import BookReviewSerializer
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy
from rest_framework import generics
from .models import BookReview
from .forms import  ReviewForm
from .serializers import BookReviewSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q 
# API View to handle BookReview operations
class BookReviewListAPIView(generics.ListCreateAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class BookReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BookReview.objects.filter(created_by=self.request.user)




class PageTitleMixin(object):
  def get_page_title(self, context):
    return getattr(self, "page_title", "Default Page Title")

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["page_title"] = self.get_page_title(context)

    return context


# Create your views here.

  
class ReviewCreateView(PageTitleMixin, LoginRequiredMixin, CreateView):
    model = BookReview
    form_class = ReviewForm  # Make sure this form exists
    template_name = 'review/create.html'  # Ensure this path is correct
    page_title = 'Review Create'
    
    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        messages.success(self.request, "Review Created successfully")  
        return super().form_valid(form)
    
class ReviewListView(PageTitleMixin, LoginRequiredMixin,ListView):
   model=BookReview
   template_name='review/list.html'
   context_object_name='reviews'
   paginate_by = 10  
   def get_queryset(self):
        return BookReview.objects.all()    

   def get_queryset(self):
        title_val = self.request.GET.get('title', '')
        author_val = self.request.GET.get('author', '')
        rating_val = self.request.GET.get('rating', '')
        new_context = BookReview.objects.all().order_by('-id')
        if(title_val!='') : 
            new_context = new_context.filter(
                Q(title__icontains=title_val)
            )
        if(author_val!='') : 
            new_context = new_context.filter(
                Q(author__contains=author_val) 
            )
        if(rating_val!='') : 
            new_context = new_context.filter(
                Q(rating_val__icontains=rating_val) 
            )
        return new_context
   def get_context_data(self, **kwargs):
        context = super(ReviewListView, self).get_context_data(**kwargs)
        context['title_val'] = self.request.GET.get('title', '')
        context['author_val'] = self.request.GET.get('author', '')
        context['rating_val'] = self.request.GET.get('rating', '')
        return context   
   

class ReviewUpdateView(UpdateView,PageTitleMixin, LoginRequiredMixin):   
    model=BookReview
    template_name='review/create.html'
    form_class=ReviewForm
    page_title='Review Update'

    def form_valid(self, form):
      messages.success(self.request, "Review updated successfully")
      return super().form_valid(form)
    

def review_delete_view(request, pk):

    # Fetch the Employee object related to the passed id
    bookreview_instance = get_object_or_404(BookReview, id=pk)
    
    # Delete the Employee object
    bookreview_instance.delete()

    messages.success(request, "Review deleted successfully")
    
    # Redirect to the 'Employee List' view or any other appropriate view
    return redirect('Review List')    