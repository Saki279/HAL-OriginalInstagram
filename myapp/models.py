from django.db import models
# ユーザー認証
from django.contrib.auth.models import User
# from myapp import Account

# ユーザーアカウントのモデルクラス
class Account(models.Model):
    

    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    account_image = models.ImageField(upload_to="profile_pics",blank=True)
    
    
    #管理画面でのデータの判別をしやすくなる
    def __str__(self):
        return self.user.username


class Post(models.Model):
   content = models.TextField()
   tagu = models.TextField()
   when = models.TextField()
   where = models.TextField()
   #user = models.ForeignKey(User, on_delete=models.CASCADE)
   post_image = models.ImageField(upload_to="post_pics", blank=True, verbose_name = 'post_image',)
   #ImageFieldにupload_toを指定すると画像をMEDIA_ROOT以下のフォルダの保存先を指定できる
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return self.user.tagu

   class Meta:
       ordering = ["-created_at"]     #投稿順にクエリを取得
       


