from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

## serializers.ModelSerializerを継承して、UserSerializerを作成する
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        ## jsonファイルの項目定義
        fields = ('id', 'username', 'password')
        ## オプション指定
        ## パスワードはクライアントから受け取るのみ、
        ## required　必須入力
        extra_kwargs = {'password':{'write_only':True, 'required':True}}

    ## serializers.ModelSerializerにcreateやupdateが含まれているが、
    ## カスタマイズしたい部分のみオーバライドする
    def create(self, validated_data):
        ## パスワードはハッシュ化して保存する
        user = User.objects.create_user(**validated_data)
        return user

class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title','finish_flg', 'created_at', 'updated_at')
