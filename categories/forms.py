from django import forms
from categories.models.product import Product
from categories.models.version import Version
from categories.list_config_name.config_name import FORBIDDEN_WORDS


class BootstrapForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})


class ProductForm(BootstrapForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data["name"].lower()
        for forbidden_word in FORBIDDEN_WORDS:
            if forbidden_word in name:
                raise forms.ValidationError("Пожалуйста, измените название.")
        return name


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ["product", "name_version", "number_version", "is_current_version"]

    def clean(self):
        cleaned_data = super().clean()
        is_active = cleaned_data.get("is_current_version")
        if is_active and self.instance.product:
            Version.objects.filter(
                product=self.instance.product, is_current_version=True
            ).exclude(pk=self.instance.pk).update(is_current_version=False)
        return cleaned_data
