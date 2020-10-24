from django.contrib import admin

from demo.models import User, Article, Comment


class Test(admin.TabularInline):
    model = User


class MyTest(admin.ModelAdmin):
    # 表头标题
    list_display = ('title', 'content', 'user')
    # action功能摆放位置
    actions_on_bottom = True
    actions_on_top = False
    # 选中条目个数的显示
    actions_selection_counter = True
    # 搜索时用到的字段
    search_fields = ('content',)
    # 对应的字段
    fieldsets = (
        [None, {"fields": ('title', 'content', 'user')}],
    )
    # 时间分层
    date_hierarchy = 'publish_date'

    def user(self, obj):
        return obj.user.username


@admin.register(User)
class TestUser(admin.ModelAdmin):
    list_display = ('username', 'email', 'gendle', 'createdate')
    search_fields = ("username", 'email')
    # 过滤器
    list_filter = ('username', 'email')
    date_hierarchy = 'createdate'
    fieldsets = (
        [None, {"fields": ('username', 'email', 'gendle', 'createdate')}],
    )


admin.site.register(Article, MyTest)


