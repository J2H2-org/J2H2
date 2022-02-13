from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, TPViewSet, MAViewSet, MQViewSet, CAViewSet, CQViewSet, ACViewSet, SRViewSet, SDViewSet, SIViewSet, SAViewSet, SA2ViewSet

app_name = 'chat_teesis'

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('plans', TPViewSet)
router.register('answers', MAViewSet)
router.register('questions', MQViewSet)

urlpatterns = [
    path('search/<slug>/', SRViewSet.as_view(), name="search"),
    path('', include(router.urls)),
    path('questions/answers/<slug:mentee_question_Id>', SearchQtoAViewSet.as_view())
    path('mentee-questions/search/', SRViewSet.as_view(), name="search"),
    path('mentee-questions/search/<slug>/', SDViewSet.as_view(), name="search-data"),
    path('mentee-questions/search/ID/<slug>/', SIViewSet.as_view(), name="search-data"),
    path('answer/search/', SA2ViewSet.as_view(), name="search-answer"),
    path('answer/search/<slug>/', SAViewSet.as_view(), name="search-answer"),
] + router.urls
                  
                  x