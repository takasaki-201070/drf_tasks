from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializer
from .models import Task

# 新規アカウント作成時用
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    # AllowAny : 誰でもアクセス可能
    permission_classes = (AllowAny,)

# ログインしているユーザのプロフィールを取得する
class MyProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user

# タスク情報をやり取りする
## viewsets.ModelViewSetを継承する事で、create,read,update,deleteの
## メソッドが定義されている(serializerの定義のみで使用できる)
class TaskViewSet(viewsets.ModelViewSet):
    # データベースに定義されている項目を全てセットする
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # 検索時はログインユーザとownerが一致するデータのみを抽出対象とする
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    # 新規作成時は、ログインユーザをownerに自動的に設定する
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
