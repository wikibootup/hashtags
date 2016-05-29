from django import forms


class SearchForm(forms.Form):
    search_tags = forms.CharField(
        widget=forms.fields.TextInput(attrs={
            'placeholder': '검색',
        }),
    )
