from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta():
        model = UserModel
        fields = '__all__'
        
        '''
        user = forms.CharField(
            label='ユーザー名',
            max_length=100
        )

        passward = forms.CharField(
            label='パスワード',
            max_length=100
        )

        twitter = forms.CharField(
            label='Twitterアドレス（任意）',
            max_length=100
        )

        email = forms.CharField(
            label='メールアドレス（任意）',
            max_length=100
        )
        

        title = forms.CharField(
            label='タイトル',
            max_length=100
        )

        movie1 = forms.CharField(label='映画１',max_length=100)
        movie2 = forms.CharField(label='映画２',max_length=100)
        movie3 = forms.CharField(label='映画３',max_length=100)
        '''

