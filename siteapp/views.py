from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.utils import timezone
from django.db.models import Q
from django.http import Http404, HttpResponseBadRequest, JsonResponse
from django.views import generic
from .forms import PostSearchForm
from .models import Post,Category


class ArchiveListMixin:
    model = Post
    paginate_by = 5
    date_field = 'published'
    template_name = 'main.html'
    allow_empty = True
    make_object_list = True

class IndexView(ArchiveListMixin, generic.ArchiveIndexView):

    def get_queryset(self):
        return super().get_queryset().select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = '最新の投稿'
        return context

class PostSearchList(ArchiveListMixin, generic.ArchiveIndexView):

    def get_queryset(self):
        queryset = super().get_queryset()
        self.request.form = form = PostSearchForm(self.request.GET)
        form.is_valid()
        self.key_word = key_word = form.cleaned_data['key_word']
        if key_word:
            queryset = queryset.filter(Q(title__icontains=key_word) | Q(text__icontains=key_word))
        return queryset.select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = '「{}」 の検索結果'.format(self.key_word)
        return context


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_object(self, queryset=None):
        post = super().get_object()
        if post.published <= timezone.now():
            return post
        raise Http404

class PostCategoryList(ArchiveListMixin, generic.ArchiveIndexView):

    def get_queryset(self):
        self.category = category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return super().get_queryset().filter(category=category).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = '「{}」 カテゴリの投稿'.format(self.category.name)
        return context

class PostYearList(ArchiveListMixin, generic.YearArchiveView):

    def get_queryset(self):
        return super().get_queryset().select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = '{}年の投稿'.format(self.kwargs['year'])
        return context

class PostMonthList(ArchiveListMixin, generic.MonthArchiveView):
    month_format = '%m'

    def get_queryset(self):
        return super().get_queryset().select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = '{}年{}月の投稿'.format(self.kwargs['year'], self.kwargs['month'])
        return context

#Googleconsole youni ireru
def google_search_console(request):
    return render(request, 'google9689b400addd4ddc.html')
