from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet)
router.register(r'stage', StageViewSet)
router.register(r'organization', OrganizationViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('tag/', TagListAPIView.as_view(), name='tag-list'),
    path('olympiads/', OlympiadListCreate.as_view()),
    path('olympiads/<int:pk>', OlympiadDetail.as_view()),

    path('materials', MaterialListCreate.as_view()),
    path('materials/<int:pk>', MaterialDetail.as_view()),

    path('shop', ProductListCreate.as_view()),
    path('shop/<int:pk>', ProductDetail.as_view()),

]