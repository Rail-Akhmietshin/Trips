from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path("", FindTripMain.as_view(), name='main'),
    path("trips/", cache_page(1)(Trips.as_view()), name='trips'),
    path('new_trip/', AddTrip.as_view(), name='new_trip'),
    path('auth/', AuthUser.as_view(), name='auth'),
    path('logout/', logout_user, name='logout'),
    path("delete_user/", delete_user, name='delete_user'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    re_path(r'^verify/(?P<uuid>[a-z0-9\-]+)/', verify, name='verify'),
    path('profile/<str:profile>/', MyProfile.as_view(), name="myprofile"),
    path('profile/<str:profile>/trips/', MyTrips.as_view(), name="mytrips"),
    path('profile/update_profile/<int:pk>', UpdateProfile.as_view(), name="update_profile"),

    # re_path(r"^trips/(?P<where_from>[0-9]{4})/", re_archive),      # задание url с помощью регулярных выражений
]



# str – любая не пустая строка, исключая символ ‘/’
#   int – любое положительное целое число, включая 0
# slug – слаг, то есть, латиница ASCII таблицы, символы дефиса и подчеркивания
#   uuid – цифры, малые латинские символы ASCII, дефис
# path – любая не пустая строка, включая символ ‘/’