from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.urls import reverse
from django.views import View

from demo import models
from demo.models import User, Article, Comment


def login_page(request):
    result = '请输入用户名、密码'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        exist_user = User.objects.filter(username=username)
        if exist_user:
            exist__password = User.objects.filter(username=username, password=password)
            if exist__password:
                request.session['userinfo'] = exist_user.first().username
                return redirect('demo:demo_home')
            else:
                result = '输入的密码有误'
        else:
            result = '输入的用户名不存在'
    else:
        result = '请输入用户名、密码'
    return render(request, 'login.html', {'result': result})


def register_page(request):
    result = '请输入用户名、密码'
    register_username = request.POST.get('register_username')
    register_password = request.POST.get('register_password')
    register_email = request.POST.get('register_email')
    exist_user = User.objects.filter(username=register_username)
    if exist_user:
        result = '用户名已存在'
        return render(request, 'register.html', {'result': result})

    if register_username != '':
        if 6 <= len(str(register_username)) <= 16 and 6 <= len(str(register_username)) <= 16:
            for i in register_username:
                if 48 <= ord(i) <= 57 or 65 <= ord(i) <= 90 or ord(i) == 95 or 97 <= ord(i) <= 122:
                    pass
                else:
                    result = "存在不合法字符"
            for i in register_password:
                if 48 <= ord(i) <= 57 or 65 <= ord(i) <= 90 or ord(i) == 95 or 97 <= ord(i) <= 122:
                    pass
                else:
                    result = "存在不合法字符"
            if result != "存在不合法字符":
                u = User()
                u.username = register_username
                u.password = register_password
                u.email = register_email
                u.gendle = request.POST.get('gendle')
                u.birth_place = request.POST.get('birth_place')
                u.university = request.POST.get('university')
                u.age = request.POST.get('age')
                u.weigth = request.POST.get('weigth')
                u.heigth = request.POST.get('heigth')
                u.language = request.POST.get('language')
                u.birthday = request.POST.get('birthday')
                u.question1 = request.POST.get('question1')
                u.answer1 = request.POST.get('answer1')
                u.question2 = request.POST.get('question2')
                u.answer2 = request.POST.get('answer2')
                u.question3 = request.POST.get('question3')
                u.answer3 = request.POST.get('answer3')
                u.save()
                result = '注册成功'
                return redirect('demo:demo_login')
        else:
            result = '请输入6-16位用户名、密码'
    else:
        result = '请输入用户名、密码'
    return render(request, 'register.html', {'result': result})


def login_or_logout(func):
    def wrapper(request, *args, **kwargs):
        username = request.session.get('userinfo')
        user = User.objects.filter(username=username).first()
        if user:
            setattr(request, 'user', user)
            result = func(request, *args, **kwargs)
            return result
        else:
            return redirect('demo:demo_login')
    return wrapper


def correction_page(request):
    result = '请输入用户名、邮箱'
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        exist_user = User.objects.filter(username=username)
        if exist_user:
            exist__email = User.objects.filter(username=username, email=email)
            if exist__email:
                question1 = User.objects.get(username=username).question1
                question2 = User.objects.get(username=username).question2
                question3 = User.objects.get(username=username).question3
                return render(request, 'correction2.html', {'question1': question1, 'question2': question2,
                                                            'question3': question3, 'username': username})
            else:
                result = '输入的邮箱有误'
        else:
            result = '输入的用户名不存在'
    else:
        result = '请输入用户名、邮箱'
    return render(request, 'correction.html', {'result': result})


def correction2_page(request):
    result = '请输入密保、新密码'
    if request.method == "POST":
        username = request.POST.get('username')
        answer1 = request.POST.get('answer1')
        answer2 = request.POST.get('answer2')
        answer3 = request.POST.get('answer3')
        new_password = request.POST.get('new_password')
        exist_username = User.objects.filter(username=username)
        if exist_username:
            exist_answer1 = User.objects.filter(username=username, answer1=answer1)
            if exist_answer1:
                exist_answer2 = User.objects.filter(username=username, answer1=answer1, answer2=answer2)
                if exist_answer2:
                    exist_answer3 = User.objects.filter(username=username, answer1=answer1, answer2=answer2, answer3=answer3)
                    if exist_answer3:
                        u = User.objects.get(username=username)
                        u.password = new_password
                        u.save()
                        return redirect('demo:demo_login')
                    else:
                        result = '密保3错误'
                else:
                     result = '密保2错误'
            else:
                result = '密保1错误'
        else:
            result = '用户名不存在'
    else:
        result = '请输入密保、新密码'
    return render(request, 'correction2.html', {'result': result})


@login_or_logout
def correction3_page(request):
    username = request.session.get('userinfo')
    qusetion1 = User.objects.get(username=username).question1
    qusetion2 = User.objects.get(username=username).question2
    qusetion3 = User.objects.get(username=username).question3
    if request.method == "POST":
        answer1 = request.POST.get('answer1')
        answer2 = request.POST.get('answer2')
        answer3 = request.POST.get('answer3')
        new_password = request.POST.get('new_password')
        exist_answer1 = User.objects.filter(username=username, answer1=answer1)
        if exist_answer1:
            exist_answer2 = User.objects.filter(username=username, answer1=answer1, answer2=answer2)
            if exist_answer2:
                exist_answer3 = User.objects.filter(username=username, answer1=answer1, answer2=answer2,
                                                    answer3=answer3)
                if exist_answer3:
                    u = User.objects.get(username=username)
                    u.password = new_password
                    u.save()
                    del request.session['userinfo']
                    return redirect('demo:demo_login')
                else:
                    result = '密保3错误'
            else:
                result = '密保2错误'
        else:
            result = '密保1错误'
    else:
        result = '请输入密保、新密码'
    return render(request, 'correction3.html', {'result': result,
                                                'question1': qusetion1,
                                                'question2': qusetion2,
                                                'question3': qusetion3})


def home_page(request):
    username = request.session.get('userinfo')
    user = User.objects.filter(username=username).first()
    if user:
        pass
    else:
        username = 'World'
    all_article = Article.objects.all()
    article_top = Article.objects.order_by('-publish_date')[:10]
    return render(request, 'home.html', {'article_list': all_article,
                                         'username': username,
                                         'article_top': article_top})


@login_or_logout
def detail_page(request, article_id):
    all_article = Article.objects.all()
    curr_article = None
    previous_article = None
    next_article = None
    for index, article in enumerate(all_article):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        if article.article_id == article_id:
            curr_article = article
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break
    section_list = curr_article.content.split('\n') if curr_article else None
    if not section_list:
        return redirect(reverse("demo:demo_home"))
    article_comment = curr_article.comment_set.all()
    return render(request, 'detail.html',
                  {
                      'curr_article': curr_article,
                      'section_list': section_list,
                      'previous_article': previous_article,
                      'next_article': next_article,
                      'article_comment':article_comment
                  })


@login_or_logout
def index_page(request):
    username = request.session.get('userinfo')
    print(username)
    information = models.User.objects.get(username=username)
    email = information.email
    gendle = information.gendle
    birth_place = information.birth_place
    university = information.university
    age = information.age
    weigth = information.weigth
    heigth = information.heigth
    language = information.language
    birthday = information.birthday
    createdate = information.createdate
    # my_article = request.session.get('userinfo').user.foreign_set.all()
    my_article = information.article_set.all()
    return render(request, 'index.html', {'email': email,
                                          'username': username,
                                          'dendle': gendle,
                                          'birth_place': birth_place,
                                          'university': university,
                                          'age': age,
                                          'heigth': heigth,
                                          'weigth': weigth,
                                          'language': language,
                                          'birthday': birthday,
                                          'createdate': createdate,
                                          'my_article': my_article})


@login_or_logout
def article_add_page(request):
    username = request.session.get('userinfo')
    information = models.User.objects.get(username=username)
    result = '请填写文章'
    if request.method == "POST":
        title = request.POST.get('title')
        brief_content = request.POST.get('brief_content')
        content = request.POST.get('content')
        article, is_create = Article.objects.get_or_create(title=title,
                                                           brief_content=brief_content,
                                                           content=content,
                                                           user_id=information.id)
        if is_create:
            result = '文章添加成功'
        else:
            result = '请填写文章'
    return render(request, 'article_add.html', {'result': result})


@login_or_logout
def article_correct_page(request):
    pass


@login_or_logout
def article_correct2_page(request):
    result = '请输入文章并按查找键执行'
    username = request.session.get('userinfo')
    information = models.User.objects.get(username=username)
    my_article = information.article_set.all()
    title = request.POST.get('title')
    brief_content = request.POST.get('brief_content')
    content = request.POST.get('content')
    if request.method == "POST":
        article = my_article.filter(title=title).first()
        if article:
            article.title = title
            article.brief_content =brief_content
            article.content = content
            article.save()
            result = '修改成功'
        else:
            result = '您没有发表过此文章'
    return render(request, 'article_correct2.html', {'result': result, 'username': username})


@login_or_logout
def article_delete_page(request):
    result = '请输入文章标题并按删除键执行'
    username = request.session.get('userinfo')
    information = models.User.objects.get(username=username)
    my_article = information.article_set.all()
    article_title = request.POST.get('article_title')
    if request.method == "POST":
        article = my_article.filter(title=article_title).first()
        if article:
            article.delete()
            result = '删除成功'
        else:
            result = '您没有发表过此文章'
    return render(request, 'article_delete.html', {'result': result, 'username': username})


@login_or_logout
def logout_page(request):
    result = '点击确认即可退出'
    username = request.session.get('userinfo')
    if request.method == "POST":
        del request.session['userinfo']
        return render(request, 'login.html')
    return render(request, 'logout.html', {'result': result, 'username': username})


@login_or_logout
def comment_add_page(request):
    username = request.session.get('userinfo')
    article_id = request.POST.get('article_id')
    if request.method == "POST":
        comment = request.POST.get('comment')
        user_comment = username + '：' +comment
        article_id = request.POST.get('article_id')
        c = Comment()
        c.comment = user_comment
        c.article_id = article_id
        c.save()
    return render(request, 'comment_add.html', {'username': username})


@login_or_logout
def comment_delete_page(request):
    username = request.session.get('userinfo')
    article_id = request.POST.get('article_id')
    if request.method == "POST":
        comment = request.POST.get('comment')
        article_id = request.POST.get('article_id')
        comment_delete = Comment.objects.filter(comment=comment).first()
        comment_delete.delete()
    return render(request, 'comment_delete.html', {'username': username, 'article_id': article_id})


def home(request):
    return redirect('/demo/home')



