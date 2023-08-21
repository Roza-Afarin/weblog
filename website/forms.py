from django import forms
from website.models import contact
from captcha.fields import CaptchaField


class ContactForm(forms.ModelForm):
    subject = forms.CharField()
    captcha = CaptchaField()
    class Meta:
        model = contact
        fields = '__all__'

