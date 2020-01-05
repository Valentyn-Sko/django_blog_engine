from django import forms
from django.core.exceptions import ValidationError
from .models import Tag


class TagForm(forms.ModelForm):
    #                   forms.Form
#    title = forms.CharField(max_length=50)
#    slug = forms.CharField(max_length=50)
#
#    title.widget.attrs.update({'class': 'form-control'})
#    slug.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data.get('slug').lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        elif Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_slug))
        return new_slug
    # forms.Form without UPDATE
    #def save(self):
    #    new_tag = Tag.objects.create(
    #        title=self.cleaned_data['title'],
    #        slug=self.cleaned_data['slug']
    #    )
    #    return new_tag


class PostForm(forms.Form):
    title = forms.CharField(max_length=150)
    slug = forms.CharField(max_length=150)
    body = forms.Textarea()
