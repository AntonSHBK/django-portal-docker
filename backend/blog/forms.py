
from ckeditor.widgets import CKEditorWidget

from django import forms

from blog.models import Post


class NewPostForm(forms.Form):
    title = forms.CharField(
        max_length=200, 
        label="Title article",
    )
    content = forms.CharField(
        max_length=5000,
        label="Text article",
        widget=CKEditorWidget(),
    )
    
    
class NewPostModelForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'content')
        # exclude = ()
        verbose_name = 'New post'
        verbose_name_plural = 'New posts'
    
    def __init__(self,  *args, **kwargs) -> None:
        self.user = kwargs.pop('user')
        super(NewPostModelForm, self).__init__(*args, **kwargs)
        
    #  функция для проверки поля title
    def clean_title(self):
        title = self.cleaned_data['title']
        if Post.objects.filter(author=self.user, title=title).exists():
            raise forms.ValidationError("You have already written a article with same title.")
        return title
    