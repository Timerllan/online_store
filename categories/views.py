from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from categories.models.product import Product
from categories.models.category import Category
from categories.models.version import Version
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from categories.forms import ProductForm, VersionForm
from django.forms.models import inlineformset_factory


class ProductListView(ListView):
    model = Product
    context_object_name = "object_list"

    def get_queryset(self):
        category_id = self.request.GET.get("category")

        # Начинаем с полного списка опубликованных продуктов
        queryset = Product.objects.filter(is_published=True).prefetch_related(
            "versions"
        )

        # Фильтрация по категории, если она указана
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("categories:product_store")

    def form_valid(self, form):
        # Устанавливаем автора на текущего пользователя
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("categories:product_store")
    permission_required = "categories.change_product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(
            Product,
            Version,
            form=VersionForm,
            extra=1,
            can_delete=True,
        )

        if self.request.POST:
            context["formset"] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context["formset"] = VersionFormset(instance=self.object)

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)  # Сохраняем основной объект
        formset = self.get_context_data()["formset"]

        if formset.is_valid():
            self.object.save()  # Сохраняем основной объект
            formset.instance = self.object  # Привязываем версии к объекту
            formset.save()  # Сохраняем версии
            return super().form_valid(form)  # Перенаправляем после успешного сохранения
        else:
            return self.form_invalid(form)  # Если форма не валидна, возвращаем ошибки

    def dispatch(self, request, *args, **kwargs):
        # Получаем объект продукта
        self.object = self.get_object()

        # Сравниваем автора с текущим пользователем
        if self.object.author != request.user:
            return HttpResponseForbidden(
                "Вы не имеете прав для редактирования этого продукта."
            )

        return super().dispatch(request, *args, **kwargs)
