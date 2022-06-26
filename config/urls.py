from django.contrib import admin
from django.urls import path
import api.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', views.initial_form, name='initial_form'),
    path('api/v1/<str:coin>/<str:quantity>/', views.get_info_coin_by_code_and_quantity,
         name="get_info_coin_by_code_and_quantity"),
    path('api/v1/<str:coin>/<int:days>/',
         views.get_info_coin_by_code_and_days,
         name="get_info_coin_by_code_and_days"),
    path('api/v1/<str:coin>/',
         views.get_info_coin_by_code_in_realtime,
         name="get_info_coin_by_code_in_realtime")

]
