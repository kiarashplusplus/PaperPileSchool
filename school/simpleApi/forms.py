from django.forms import ModelForm
from .models import Gradeable


class GradeableForm(ModelForm):
    class Meta:
        model = Gradeable
        fields = ['name', 'document', 'student']
