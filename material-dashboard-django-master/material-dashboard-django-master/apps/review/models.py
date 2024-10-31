# author Osada Thilan Vimukthi 
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from django_currentuser.db.models import CurrentUserField
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.

from django.conf import settings
from django.db import models

class BookReview(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False)
    author = models.CharField(max_length=20, null=False, blank=False)
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    review_text = models.CharField(max_length=500, null=False, blank=False)
    
    # Add a related_name to avoid reverse accessor clashes
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='book_reviews_created', on_delete=models.DO_NOTHING, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Add a related_name to avoid reverse accessor clashes
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='book_reviews_modified', on_delete=models.DO_NOTHING, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):       
        return reverse('Review Update', kwargs={'pk': self.pk}) 


