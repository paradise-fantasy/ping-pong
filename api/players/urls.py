from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from players import views

urlpatterns = [
    url(r'^players/$', views.PlayerList.as_view()),
    url(r'^players/(?P<pk>[0-9]+)/$', views.PlayerDetail.as_view()),
    url(r'^players/(?P<player_key_1>[0-9]+)/(?P<player_key_2>[0-9]+)$', views.PlayerRatingPotential.as_view()),

    url(r'^me/(?P<cardid>.+)/$', views.MeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
