from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter your name',
            'name': "name",
            'maxlength': "100"
        }
    ))
    email = forms.EmailField(label="", widget=forms.EmailInput(
        attrs={
            'placeholder': 'Enter your email',
            'name': "email",
            'maxlength': "250"
        }
    ))
    website = forms.URLField(label="", widget=forms.URLInput(
        attrs={
            'placeholder': 'example@example.com',
            'name': "website"
        }
    ))
    message = forms.CharField(label="", widget=forms.Textarea(attrs={
                'placeholder': 'Enter your message',
                'name': "message",
                'maxlength': "500"
            }
        ))
