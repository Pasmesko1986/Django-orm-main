from django.urls import path
from e_commerce.views import *


urlpatterns = [
    path('comic-list/', comic_list_api_view),
    path('comic-retrieve/', comic_retrieve_api_view),
    path('comic-create/', comic_create_api_view)
]
