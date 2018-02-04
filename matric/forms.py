from django import forms

from .models import SchoolRecord

class SchoolRecordForm(forms.ModelForm):

    class Meta:
        model = SchoolRecord
        fields = ('emis','centre_no', 'name', 'wrote_2014','passed_2014', 'wrote_2015','passed_2015', 'wrote_2016','passed_2016')