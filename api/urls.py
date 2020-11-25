from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import TaskViewSet, CreateUserView, MyProfileView

# viewsets.ModelViewSetを継承したclassはrouterに登録可能
router = routers.DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')

# genericsを継承したclassは、下記に追加する
urlpatterns = [
    path('myself/', MyProfileView.as_view(), name='myself'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('', include(router.urls)),
]
