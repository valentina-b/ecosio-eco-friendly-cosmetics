from django import forms

from .models import Blog


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['autofocus'] = True
        self.fields['slug'].widget.attrs['placeholder'] = 'ending of the link'
        self.fields['intro_paragraph'].widget.attrs['placeholder'] = '100 - 400 characters'
        self.fields['blog_content_1'].widget.attrs['placeholder'] = 'min 250 characters'
        self.fields['blog_content_2'].widget.attrs['placeholder'] = 'min 250 characters'
        self.fields['blog_content_3'].widget.attrs['placeholder'] = 'min 250 characters'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'add-blog-form-field'
