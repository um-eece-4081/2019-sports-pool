from django import forms

class GameModelChoiceField(forms.Form):
    Games_form = forms.ModelMultipleChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


