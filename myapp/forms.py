from django import forms
from django.contrib.auth.models import User
from .models import Account
from .models import Post


# フォームクラス作成
class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    # password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username','password')
        # フィールド名指定
        # labels = {'username':"ユーザーID",'email':"メール"}
        
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password',
                   'class': 'pass'}))
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Username',
                   'class': 'un'}))    
    

class AddAccountForm(forms.ModelForm):
    class Meta():
        # モデルクラスを指定
        model = Account
        fields = ('account_image',)
        # labels = {'account_image':"写真アップロード"}
        
        

class PostForm(forms.ModelForm):
    
    
        # フォームを綺麗にするための記載
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['content'].widget.attrs['class'] = 'description'
        # self.fields['tagu'].widget.attrs['class'] = 'tagu'
        # self.fields['when'].widget.attrs['class'] = 'when'
        # self.fields['where'].widget.attrs['class'] = 'where'
        self.fields['content'].widget = forms.Textarea(attrs={'class': 'description'})
        self.fields['tagu'].widget = forms.Textarea(attrs={'class': 'tagu', 'placeholder': 'ハッシュタグ'})
        self.fields['when'].widget = forms.Textarea(attrs={'class': 'when', 'placeholder': 'いつ'})
        self.fields['where'].widget = forms.Textarea(attrs={'class': 'where', 'placeholder': 'どこで'})
        for field in self.fields.values():
            # field.widget.attrs['class'] = 'tabs'
            #  placeholderにフィールドのラベルを入れる
            field.widget.attrs['placeholder'] = field.label



    
    class Meta:
        
        # どのモデルをフォームにするか指定
        model = Post
        # そのフォームの中から表示するフィールドを指定
        fields = ('content', 'tagu', 'when', 'where', 'post_image',)
        

        
        post_image = forms.ImageField(required=True)
        
        # content = forms.CharField(
        #     widget=forms.TextInput()
        # )

        # tagu = forms.CharField(
        #     widget=forms.Textarea(
        #         attrs={'placeholder': 'ハッシュタグ',
        #                'class': 'tagu'}))
        
        # when = forms.CharField(
        #     widget=forms.Textarea(
        #         attrs={'placeholder': 'いつ',
        #                'class': 'when'}))
        
        # where = forms.CharField(
        #     widget=forms.Textarea(
        #         attrs={'placeholder': 'どこで',
        #                'class': 'where'}))

    # フォームを綺麗にするための記載
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.fields['content'].widget = forms.TextInput(attrs={'class': 'description', 'placeholder': '投稿文'})
        #     self.fields['tagu'].widget = forms.TextInput(attrs={'class': 'tagu', 'placeholder': 'ハッシュタグ'})
        #     self.fields['when'].widget = forms.TextInput(attrs={'class': 'when', 'placeholder': 'いつ'})
        #     self.fields['where'].widget = forms.TextInput(attrs={'class': 'where', 'placeholder': 'どこで'})
        #     for field in self.fields.values():
        #         field.widget.attrs['class'] = 'tabs'
        #         #  placeholderにフィールドのラベルを入れる
        #         field.widget.attrs['placeholder'] = field.label