from django import forms


class SearchForm(forms.Form):
    search_tag = forms.CharField(
        widget=forms.fields.TextInput(attrs={
            'placeholder': '검색',
        }),
    )
