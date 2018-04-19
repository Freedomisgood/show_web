from django import forms
from . import models
class Msgform(forms.ModelForm):
    class Meta:
        model = models.msg
        fields = ['text']

    def __init__(self,*args,**kwargs):
        super(Msgform,self).__init__(*args,**kwargs)
        self.fields['text'].label = '聊天记录'

class InfoForm(forms.Form):
    data = forms.CharField(label='出生日期')
    sexy = forms.CharField(label='性别')
    love = forms.CharField(max_length=20)

class LoginForm(forms.Form):
    username = forms.CharField(label='姓名',max_length=10)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
