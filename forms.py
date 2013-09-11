from django import newforms as forms

class SubscriberForm(forms.Form):
	email = forms.EmailField(label='Email')
