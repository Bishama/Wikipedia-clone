from django import forms

class EntryForm(forms.Form):
    title = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Title",
                    "class":"form-control m-2"
            }
        )
    )

    content = forms.CharField(
        required=True,
        label="",
        widget=forms.Textarea(
        attrs={"placeholder": 'Content',
        "class":"form-control m-2"}
    )
    )



class EditForm(forms.Form):
    content = forms.CharField(
        label="",
        widget=forms.Textarea(
        attrs={"placeholder": 'Content',
        "class":"form-control m-2"}
    )
    )


