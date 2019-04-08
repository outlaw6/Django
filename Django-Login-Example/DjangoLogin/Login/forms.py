from django import forms
from Login.models import Name

class NewUser(forms.ModelForm): # .ModelForm to connect form to db

    class Meta:
        model = Name
        fields = '__all__' # using all fields from forms
