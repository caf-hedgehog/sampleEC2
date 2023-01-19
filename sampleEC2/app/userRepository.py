from .models import users


class userRepository(object):
    """description of class"""

    # ユーザー登録
    def insert(request):
        data = request.POST
        print(data["name"])
        print(str(data["password"]))
        users.objects.create(
            name=data["name"], email=data["email"], password=str(data["password"])
        )

    # ユーザー検索
    def load(_email):
        user = users.objects.get(email=_email)
        print(user.email)
        return user
