from django.contrib import admin
from .models import Section, ArticleType, Article, Status


admin.site.register([Section, ArticleType, Article, Status])
