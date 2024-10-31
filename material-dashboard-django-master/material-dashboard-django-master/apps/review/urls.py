from django.urls import path

from apps.review.views import BookReviewDetailAPIView, ReviewCreateView,BookReviewListAPIView,ReviewListView,ReviewUpdateView,review_delete_view

urlpatterns = [
    path('create', ReviewCreateView.as_view(), name= "Review Create"),
    path('list',ReviewListView.as_view(), name="Review List"),
    path('update/<int:pk>/', ReviewUpdateView.as_view(), name='Review Update'),
    path('delete/<int:pk>/', review_delete_view,name='Review Delete'),
    
    
    ##API
    path('api/reviews/', BookReviewListAPIView.as_view(), name='api_bookreview_list'), 
    path('api/reviews/<int:pk>/', BookReviewDetailAPIView.as_view(), name='api_bookreview_detail'),
]
