from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import (CommentViewSet, FollowListCreateView, GroupViewSet,
                       PostViewSet)

app_name = 'api'

router = SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')
router.register(r'groups', GroupViewSet)


urlpatterns = [
    path('follow/', FollowListCreateView.as_view()),
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
