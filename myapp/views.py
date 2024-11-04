from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, FormView
from django.urls import reverse_lazy

# ログイン・ログアウト処理に利用
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import AccountForm, AddAccountForm # ユーザーアカウントフォーム
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

#投稿
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post



# class Login(LoginView):
#     template_name = "index.html"
#     form_class = LoginForm

class SignIn(TemplateView):
    template_name = "index.html"
class Home(TemplateView):
    template_name = "home.html"
class Register(TemplateView):
    template_name = "register.html" 
class Artist(TemplateView):
    template_name = "artist.html"  
class Friend(TemplateView):
    template_name = "friend.html"  
class Discover(TemplateView):
    template_name = "discover.html"  
class Post(TemplateView):
    template_name = "post.html"  
class Recommend(TemplateView):
    template_name = "recommend.html"  
class Myaccount(TemplateView):
    template_name = "myaccount.html"     
class Favorite(TemplateView):
    template_name = "favorite.html"  
 
 


#ログイン
def Login(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('username')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('myapp:home'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("アカウント名またはパスワードが間違っています")
    # GET
    else:
        return render(request, 'index.html')
    
#ホーム
@login_required
def home(request):
    params = {"UserID":request.user,}
    return render(request, "home.html",context=params)
    
    
    
#新規登録        
class  AccountRegistration(TemplateView):
    
    template_name = "register.html"
    
    field = ('username','password')

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        "add_account_form":AddAccountForm(),
        }

    # Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request,"register.html",context=self.params)

    # Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)

        # フォーム入力の有効検証
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # 下記追加情報
            # 下記操作のため、コミットなし
            add_account = self.params["add_account_form"].save(commit=False)
            # AccountForm & AddAccountForm 1vs1 紐付け
            add_account.user = account

            # 画像アップロード有無検証
            if 'account_image' in request.FILES:
                add_account.account_image = request.FILES['account_image']

            # モデル保存
            add_account.save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"register.html",context=self.params)
    
    
from django.contrib import messages
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import PostForm
from .models import Post
 
class CreatePost(CreateView):
    # LoginRequiredMixinはログインを必須にするためのもの
    # LoginRequiredMixin → TemplateView この順番で記述しないとログイン必須機能が表れない
    
    # """投稿フォーム"""
#    class Meta(): 
#         model = Post
#         template_name = 'post.html'
#         fields = ['content', 'tagu']
#         success_url = reverse_lazy('myapp:myaccount')


   model = Post
   form_class = PostForm
   template_name = "post.html"
   
   def __init__(self):
        self.params = {
        "post_form": PostForm(),
        }

    # Get処理
   def get(self,request):
        self.params["post_form"] = PostForm()
        return render(request,"post.html",context=self.params)

    # Post処理
   def post(self,request):
        self.params["post_form"] = PostForm(data=request.POST)
        
        # フォーム入力の有効検証
        if self.params["post_form"].is_valid():
            # アカウント情報をDB保存
            post = self.params["post_form"].save()


            # 画像アップロード有無検証
            if 'account_image' in request.FILES:
                post.post_image = request.FILES['post_image']

            # モデル保存
            post.save()

            # アカウント作成情報更新
            # self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["post_form"].errors)

        return render(request,"myaccount.html",context=self.params)
   
       
   # 投稿に成功した時のURL
#    success_url = reverse_lazy('myapp:myaccount')      
#    # 投稿に成功した時に実行される処理
#    def get_success_url(self):
#        messages.success(self.request, '記事を投稿しました。')
#        return resolve_url('myapp:myaccount')
   
   #バリデーションを通ったとき    
   def form_valid(self, form):
    # """投稿ユーザーをリクエストユーザーと紐付け"""
       form.instance.user = self.request.user
       messages.success(self.request, "保存しました")
       return super().form_valid(form)
    #    form_validメソッドは、ユーザーが投稿した瞬間にデータベースに投稿者情報を自動追加する
       #form.instance.(フィールド名)でデータベースのテーブル情報にアクセス   
       
   #バリデーションに失敗したとき    
   def form_invalid(self, form):
       messages.warning(self.request, "保存できませんでした")
       return super().form_invalid(form)
       
       
       
class MyPost(LoginRequiredMixin, ListView):
   # """自分の投稿のみ表示"""
   model = Post
   template_name = 'myaccount.html'

#    def get_queryset(self):
#     #自分の投稿に限定
#     return Post.objects.filter(user=self.request.user)



class appload (LoginRequiredMixin,CreateView):
    model=Post
    template_name='post.html'
    fields = ['post_image', 'content', 'tagu']
    success_url = '/list/' #mypostの関数
    
    def form_valid(self, form):
    # """投稿ユーザーをリクエストユーザーと紐付け"""
       form.instance.user = self.request.user
       return super().form_valid(form)