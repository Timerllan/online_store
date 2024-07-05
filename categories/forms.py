from django import forms
from categories.models.product import Product
from categories.list_config_name.config_name import FORBIDDEN_WORDS


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"



    def clean_name(self):  # валидация данных - проверка запрещённых слов
        name = self.cleaned_data["name"].lower()
        for forbidden_word in FORBIDDEN_WORDS:
            if forbidden_word in name:
                raise forms.ValidationError("Пожалуйста, измените название.")
        return name
