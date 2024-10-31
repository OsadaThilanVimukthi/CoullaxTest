from django import forms
from django.forms import ModelForm
from crispy_forms.layout import Layout, Submit, Row, Column, Div, Fieldset, HTML
from crispy_forms.helper import FormHelper
from apps.review.models import BookReview



class ReviewForm(ModelForm):
    class Meta:
        model = BookReview
        fields = '__all__'
        widgets={
            'title':forms.TextInput(
                attrs={
                    'class':'form-control'
                    }
                ),  
            'author': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'rating':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'review_text': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'created_by': forms.HiddenInput(),
            'created_at': forms.HiddenInput(),             
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(
                    Row(
                        Column('title', css_class = 'form-group col-md-4 mb-0'),
                        Column('author', css_class = 'form-group col-md-4 mb-0'),
                        Column('rating', css_class = 'form-group col-md-4 mb-0'),
                        css_class='form-row'
                    ),
                    Row(
                        Column('review_text', css_class = 'form-group col-md-12 mb-0'),
                       
                        
                        class_css = 'form-row'
                    ),

                    css_class='card-body',                   

                ),
                css_class='card',
            ),
            Row(
                Column(
                    Submit('submit', 'Submit'),css_class = 'text-end'
                ),
                css_class='form-row'
            )
        )
