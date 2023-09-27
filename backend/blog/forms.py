
from ckeditor.widgets import CKEditorWidget

from django import forms

class NewPost(forms.Form):
    title = forms.CharField(
        max_length=200, 
        label="Title article",
    )
    content = forms.CharField(
        max_length=5000,
        label="Text article",
        widget=CKEditorWidget()
    )
    
    
    pass