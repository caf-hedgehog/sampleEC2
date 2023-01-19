from django.shortcuts import render
from django.http.response import HttpResponse
from .sampleForm import sampleForm
from .models import users
from .userRepository import userRepository


# ログイン処理
def login(request):
    if request.method == "POST":
        error = {"loginError": "メールアドレスまたはパスワードが違います"}
        try:
            user = userRepository.load(request.POST["email"])
            if request.POST["password"] == user.password:
                return render(request, "app/user-list.html")
            else:
                return render(request, "app/login.html", error)
        except:
            return render(request, "app/login.html", error)

    return render(request, "app/login.html")


# ユーザー登録処理
def register(request):
    if request.method == "POST":
        userRepository.insert(request)
        return render(request, "app/login.html")

    return render(request, "app/register.html")


# ユーザー一覧表示処理
def userList(request):
    return render(request, "app/user-list.html")
