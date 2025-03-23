from django import forms
from .models import Review, Company

class ReviewForm(forms.ModelForm):
    JOB_TYPE_CHOICES = [
        ('การตลาด', 'การตลาด'),
        ('วิศวกรรม', 'วิศวกรรม'),
        ('ไอที', 'ไอที'),
        ('บัญชี', 'บัญชี'),
        ('อื่นๆ', 'อื่นๆ'),
    ]

    job_type = forms.ChoiceField(choices=JOB_TYPE_CHOICES, required=True)

    RECOMMEND_CHOICES = [
        (True, 'แนะนำ'),
        (False, 'ไม่แนะนำ'),
    ]

    recommend = forms.ChoiceField(choices=RECOMMEND_CHOICES, required=True)

    class Meta:
        model = Review
        fields = ['company', 'recommend', 'overall_rating', 'benefits_rating', 'environment_rating', 'management_rating', 'job_type', 'job_description', 'experience', 'advice']
        widgets = {
            'overall_rating': forms.HiddenInput(),
            'benefits_rating': forms.HiddenInput(),
            'environment_rating': forms.HiddenInput(),
            'management_rating': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].queryset = Company.objects.all()