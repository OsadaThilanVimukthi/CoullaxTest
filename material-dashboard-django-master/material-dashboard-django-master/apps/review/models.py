# author Osada Thilan Vimukthi 
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from django_currentuser.db.models import CurrentUserField

# Create your models here.

class BookReview(models.Model):
    title = models.CharField(max_length=20,blank=False,null=False)
    author = models.CharField(max_length=20,null=False,blank=False)
    rating =models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    review_text = models.CharField(max_length=500,null=False,blank=False)
    created_by = CurrentUserField(related_name='%(class)s_requests_created', on_delete=models.DO_NOTHING, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = CurrentUserField(on_update=True, on_delete=models.DO_NOTHING, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)
   


