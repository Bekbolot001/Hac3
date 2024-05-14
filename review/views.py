from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import  api_view
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated


from books.models import Books
from .models import Like, Comment, Rating, Favorite
from .serializers import CommentSerilalizer, RatingSerializer, FavoriteSerializer
from .permissions import IsOwnerOrReadOnly

@api_view(['POST']) 
def toggle_like(request, id): 
    user = request.user
    if not user.is_authenticated:
        return Response(status=401)
    car = get_object_or_404(Books, id=id)
    if Like.objects.filter(user=user, car=car).exists():
        Like.objects.filter(user=user, car=car).delete()        
    else:
        Like.objects.create(user=user, car=car)
    return Response('201')


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerilalizer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        elif self.action in ['create']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update']:
            self.permission_classes = [IsOwnerOrReadOnly]
        return [permission() for permission in self.permission_classes]    
    
class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

class FavoriteViewSet(ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer  

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [IsAuthenticated]  # Доступ только зарегистрированным пользователям
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsOwnerOrReadOnly]  # Доступ только владельцам избранных товаров
        return [permission() for permission in self.permission_classes]
