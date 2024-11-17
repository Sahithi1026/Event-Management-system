# events/forms.py
from django import forms
from .models import Event, Registration

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['college_name', 'college_code', 'event_details', 'event_image', 'college_address', 'contact_info']


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['student_name', 'student_college', 'student_email', 'number_of_participants', 'participants_emails']


class RegistrationForms(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    email = forms.EmailField(required=True)
