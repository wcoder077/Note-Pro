from django import forms
from .models import NoteData

class NotesForm(forms.ModelForm):
		
		class Meta:
				model = NoteData 
				fields = ("title","content")
