from django import forms
from pybo.models import Question,Answer

# forms에는 forms.Form과 froms.ModelForm이 있다. 
# ModelForm이 모델에 바로 저장할 수 있는 기능이 있다. 
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }
        labels = {
            'subject': '제목',
            'content': '내용',
        }  

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content' : '답변 내용',
        }