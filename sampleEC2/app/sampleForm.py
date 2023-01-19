from django import forms


class sampleForm(forms.Form):
    name = forms.CharField(label="名前")
    email = forms.CharField(label="メールアドレス")
    password = forms.CharField(label="パスワード")
