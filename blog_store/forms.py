from django import forms
from .models import BlogPost


class BlogBaseForm:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class BlogForms(BlogBaseForm, forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            "title",
            "content",
            "preview",
        ]
