from django.db import models

# Create your models here.


class User(models.Model):
    # 用户名
    username = models.CharField(max_length=30, null=True)
    # 密码
    password = models.CharField(max_length=30, null=True)
    # 邮箱
    email = models.EmailField(null=True, unique=None)
    # 性别
    gendle = models.CharField(max_length=30, null=True)
    # 籍贯
    birth_place = models.CharField(max_length=30, null=True)
    # 学历
    university = models.CharField(max_length=10, null=True)
    # 年龄
    age = models.CharField(max_length=30, null=True)
    # 体重
    weigth = models.CharField(max_length=30, null=True)
    # 身高
    heigth = models.CharField(max_length=30, null=True)
    # 语言
    language = models.CharField(max_length=10, null=True)
    # 出生日期
    birthday = models.CharField(max_length=30, null=True)
    # 帐号申请时间
    createdate = models.DateTimeField(auto_now=True)

    # 密保问题1
    question1 = models.CharField(max_length=30, null=True)
    answer1 = models.CharField(max_length=30, null=True)
    # 密保问题2
    question2 = models.CharField(max_length=30, null=True)
    answer2 = models.CharField(max_length=30, null=True)
    # 密保问题3
    question3 = models.CharField(max_length=30, null=True)
    answer3 = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.username


class Article(models.Model):
    # 文章的唯一ID
    article_id = models.AutoField(primary_key=True)
    # 文章标题
    title = models.TextField()
    # 文章的内容摘要
    brief_content = models.TextField()
    # 文章的主要内容
    content = models.TextField()
    # 文章的发布日期
    publish_date = models.DateTimeField(auto_now=True)
    # 设置为user的一对多外键
    user = models.ForeignKey('User', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Comment(models.Model):
    # 文章评论
    comment = models.TextField(null=False)
    # 设置为article的一对多外键
    article = models.ForeignKey('Article', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.comment
