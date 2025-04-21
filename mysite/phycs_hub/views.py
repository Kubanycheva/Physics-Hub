from django.shortcuts import render
from rest_framework import viewsets, generics, status

from .permissions import HasPermission
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({'detail': 'Неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class TagListAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class MaterialListCreate(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.required_permission = 'materials.add_material'
            return [IsAuthenticated(), HasPermission()]
        return []


class MaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

    def get_permissions(self):
        perms = {
            'PUT': 'materials.change_material',
            'DELETE': 'materials.delete_material',
        }
        method = self.request.method
        if method in perms:
            self.required_permission = perms[method]
            return [IsAuthenticated(), HasPermission()]
        return []

class OlympiadListCreate(generics.ListCreateAPIView):
    queryset = Olympiad.objects.all()
    serializer_class = OlympiadListSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.required_permission = 'olympiads.add_olympiad'
            return [IsAuthenticated(), HasPermission()]
        return []


class OlympiadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Olympiad.objects.all()
    serializer_class = OlympiadDetailSerializer

    def get_permissions(self):
        perms = {
            'PUT': 'olympiads.change_olympiad',
            'DELETE': 'olympiads.delete_olympiad',
        }
        method = self.request.method
        if method in perms:
            self.required_permission = perms[method]
            return [IsAuthenticated(), HasPermission()]
        return []


class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.required_permission = 'shop.add_product'
            return [IsAuthenticated(), HasPermission()]
        return []


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        perms = {
            'PUT': 'shop.change_product',
            'DELETE': 'shop.delete_product',
        }
        method = self.request.method
        if method in perms:
            self.required_permission = perms[method]
            return [IsAuthenticated(), HasPermission()]
        return []
