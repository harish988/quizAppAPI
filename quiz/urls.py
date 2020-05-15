"""quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from question.views import quiz, questions_with_answers
from score.views import user_answer
from user.views import user, unique_username, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path("quiz", quiz, name="quiz"),
    path("questions/<int:quiz_id>", questions_with_answers, name="questions_with_answers"),
    path("questions/<int:quiz_id>/<int:question_id>", questions_with_answers, name="questions_with_answers"),
    path("user-answer", user_answer, name="user_answer"),
    path("user", user, name="user_answer"),
    path("user/unique", unique_username, name="unique_username"),
    path("user/login", login, name="login"),
]
