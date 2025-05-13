from django import forms
from .models import Yorum

class YorumForm(forms.ModelForm):
    class Meta:
        model = Yorum
        fields = ['isim', 'icerik']
        widgets = {
            'isim': forms.TextInput(attrs={'placeholder': 'Adınız'}),
            'icerik': forms.Textarea(attrs={'placeholder': 'Yorumunuz'}),
        }
