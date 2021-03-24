from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from post.models import Post
from post.permissions import IsOwnerOrAdmin
from post.serializers.default import PostSerializer

User = get_user_model()


class GetCreatePostsView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GetEditDeletePostView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]


class ToggleLikePostView(GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        if user in instance.liked_by.all():
            instance.liked_by.remove(user)
        else:
            instance.liked_by.add(user)
        return Response(self.get_serializer(instance).data)


class GetLikedPostsView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(liked_by=self.request.user)


class GetUserPostsView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(author=self.kwargs.get('pk'))
        # return User.objects.get(id=self.kwargs.get('pk')).posts  This works too!


class PostsOfPeopleIAmFollowingView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    # queryset = Post.objects.all()

    # def filter_queryset(self, queryset):
    #     return self.queryset.filter(author__in=self.request.user.following.all())

    def get_queryset(self):
        return Post.objects.all().filter(author__in=self.request.user.following.all())
