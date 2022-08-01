
from logging import PlaceHolder
from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea
                              (attrs={'rows':5,'Placeholder':'Tell me: what is in ur mind?!'}),max_length=4000,help_text='Max length is 4000 charcters')
    class Meta:
        model = Topic
        fields = ['subject','message']