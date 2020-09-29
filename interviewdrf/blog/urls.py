from rest_framework import routers

from blog.views import BlogViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'comments', CommentViewSet)
urlpatterns = router.urls
