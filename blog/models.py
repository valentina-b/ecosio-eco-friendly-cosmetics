from django.db import models

from django.core.validators import MinLengthValidator


class Blog(models.Model):

    class Meta:
        ordering = ['-published_date']

    published_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=55)
    author = models.CharField(max_length=55, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    header_image = models.ImageField()
    intro_paragraph = models.TextField(validators=[MinLengthValidator(100)], max_length=400)
    subheading_1 = models.CharField(max_length=55)
    blog_content_1 = models.TextField(validators=[MinLengthValidator(250)])
    subheading_2 = models.CharField(max_length=55)
    blog_content_2 = models.TextField(validators=[MinLengthValidator(250)])
    subheading_3 = models.CharField(max_length=55, null=True, blank=True)
    blog_content_3 = models.TextField(validators=[MinLengthValidator(250)], null=True, blank=True)

    def __str__(self):
        return self.title
