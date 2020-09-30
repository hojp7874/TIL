from django import forms
from .models import Article

# # Django Model Form
# # 모델링 정보가 없을 때
# class ArticleForm(forms.Form):
#     REGION_A = 'seoul'
#     REGION_B = 'deajeon'
#     REGIONS = [
#         (REGION_A, '서울'),
#         (REGION_B, '대전'),
#     ]

#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     region = forms.ChoiceField(choices=REGIONS, widget=forms.RadioSelect)


# Django Form
# 모델링 정보 있을 때, 모델링 정보 기반으로 Django Form 생성
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(attrs={
            'class': 'my-title',
            'placeholder': '제목을 입력해주세요',
            'maxlength': 10
        })
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={
            'class': 'ny-context form-control',
            'rows':5,
            'cols':50,
        }),
        error_messages={
            'required': '내용 넣어라...'
        }
    )


    class Meta:
        model = Article
        fields = '__all__'