from django import forms
from .models import Profile

class ImageUploadForm(forms.Form):
	#print ('test3',forms.Form)

	class Meta:
		model= Profile
		#fields = ('picture,')
	#imageForm = forms.ImageField()
	#print ('ImageForm is ',imageForm)