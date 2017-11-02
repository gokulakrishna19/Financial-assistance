from django import forms
from .models import profiles


class profileform(forms.ModelForm):
	username =forms.CharField(widget=forms.TextInput(attrs={'size':'60'})) 
	age = forms.IntegerField(widget=forms.TextInput(attrs={'size':'60'}))
	email =forms.EmailField(widget=forms.TextInput(attrs={'size':'60'}))
	profession =forms.CharField(widget=forms.TextInput(attrs={'size':'60'}))
	mobile = forms.IntegerField(widget=forms.TextInput(attrs={'size':'60'}))
	csaving = forms.IntegerField(widget=forms.TextInput(attrs={'size':'60'}))
	pmsaving = forms.IntegerField(widget=forms.TextInput(attrs={'size':'60'}))
	durinv = forms.IntegerField(widget=forms.TextInput(attrs={'size':'60'}))
	risk = forms.IntegerField(widget=forms.TextInput(attrs={'size':'60'}))

	class Meta:
		model = profiles
		fields = ('username',
					'age',
					'email',
					'profession',
					'mobile',
					'csaving',
					'pmsaving',
					'durinv',
					'risk',)
