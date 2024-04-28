"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name = "index"),
    path('submit_search',views.submit_search, name = "submit_search"),
    path('random_page_search',views.random_page_search, name = "random_page_search"),
    path('change_language',views.change_language, name = 'change_language'),
    path('language_change_page',views.language_change_page, name = 'language_change_page'),
    path('quiz',views.quiz, name = 'quiz'),
    path('quiz_result',views.quiz_result, name = 'quiz_result'),
    path('submit_answer',views.submit_answer, name = 'submit_answer'),
    path('render_question',views.render_question, name = 'render_question'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)