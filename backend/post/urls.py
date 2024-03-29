from django.urls import path

from post.views import GetCreatePostsView, GetEditDeletePostView, ToggleLikePostView, GetLikedPostsView, \
    GetUserPostsView, PostsOfPeopleIAmFollowingView

urlpatterns = [
    path('', GetCreatePostsView.as_view()),
    path('<int:pk>/', GetEditDeletePostView.as_view()),
    path('toggle-like/<int:pk>/', ToggleLikePostView.as_view()),
    path('likes/', GetLikedPostsView.as_view()),
    path('user/<int:pk>/', GetUserPostsView.as_view()),
    path('following/', PostsOfPeopleIAmFollowingView.as_view()),
    # path('search/<str:subject>', Search.as_view()), this is for additional class Search - not used!
    # below is only for documentation purpose, endpoint works without below url
    # path('?search', GetCreatePostsView.as_view()),
]

