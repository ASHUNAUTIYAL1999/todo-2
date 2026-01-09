from django import forms

class input_form(forms.Form):
    task=forms.CharField(max_length=100,label='Enter your task')
    due_date=forms.DateField(label='Due Date',widget=forms.SelectDateWidget)
    priority=forms.ChoiceField(choices=[('High','High'),('Medium','Medium'),('Low','Low')],label='Priority')
    description=forms.CharField(widget=forms.Textarea,label='Description',required=False)
    completed=forms.BooleanField(label='Completed',required=False)
    submit=forms.CharField(widget=forms.HiddenInput(),initial='submit')
