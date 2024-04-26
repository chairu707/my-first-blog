from django import forms
from django.core.files.storage import default_storage

class PostSearchForm(forms.Form):
    """検索フォーム。"""
    key_word = forms.CharField(
        label='検索キーワード',
        required=False,
    )
