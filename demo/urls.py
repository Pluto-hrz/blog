from django.urls import path, include
from demo import views
from demo.views import *

urlpatterns = [
    path('login/', login_page, name="demo_login"),
    path('logout/', logout_page, name="demo_logout"),
    path('home/', home_page, name="demo_home"),
    path('register/', register_page, name="demo_register"),
    path('index/', index_page, name="demo_index"),
    path('correction/', correction_page, name="demo_correction"),
    path('correction2/', correction2_page, name="demo_correction2"),
    path('correction3/', correction3_page, name="demo_correction3"),
    path('detail/<int:article_id>', detail_page, name="demo_detail"),
    path('article_add/', article_add_page, name="demo_article_add"),
    path('article_delete/', article_delete_page, name="demo_article_delete"),
    path('article_correct/', article_correct_page, name="demo_article_correct"),
    path('article_correct2/', article_correct2_page, name="demo_article_correct2"),
    path('comment_add/', comment_add_page, name="demo_comment_add"),
    path('comment_delete/', comment_delete_page, name="demo_comment_delete"),
    # path('article/', CreateContent.as_view(), name="demo_article"),



]