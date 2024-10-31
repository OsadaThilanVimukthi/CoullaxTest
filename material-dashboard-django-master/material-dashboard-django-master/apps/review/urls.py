from django.urls import path

from apps.review.views import BookReviewDetailAPIView, ReviewCreateView,BookReviewListAPIView

urlpatterns = [
    path('create', ReviewCreateView.as_view(), name= "Review Create"),
    path('api/reviews/', BookReviewListAPIView.as_view(), name='api_bookreview_list'), 
    path('api/reviews/<int:pk>/', BookReviewDetailAPIView.as_view(), name='api_bookreview_detail'),
]
