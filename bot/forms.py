from django import forms

class ChatWithMeForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control rounded-0','rows': 1,'name': 'message'}))
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].label = ''
    