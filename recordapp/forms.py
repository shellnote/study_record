from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["date", "what_done","what_not_done","what_learned","summary_image"]
        
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['what_done'].widget.attrs['class'] = 'what-done-field-class'
