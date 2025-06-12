from rest_framework import routers

from django.contrib import admin
from django.urls import include, path

from cats.views import AchievementViewSet, CatViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'users', UserViewSet)
router.register(r'achievements', AchievementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

''' Тестовые юзеры
{
    "username": "user1",
    "password": "!password123"
}
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0OTgxNzgwNywianRpIjoiNDA0Njg0MmIwZGY4NGNkMTg1OGU5MDZkYTY3MmI2NGMiLCJ1c2VyX2lkIjoxfQ.Gm8rMwqPqrD8xoeD3GKZ6xz_nQt4m5Avy-M1QPBl8N8",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ5ODE3ODA3LCJqdGkiOiJiYmNlZDdkZTM3Nzg0OWZmYTIyOGM3NGMyOTMzMzIwYiIsInVzZXJfaWQiOjF9.2o2CiBdRiSZJ7_TowpA_tpLDwMD--qcY_Xzo64jdlTk"
}

{
    "username": "user2",
    "password": "!password123"
}
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0OTgxNzgzMCwianRpIjoiZDY4ZTAwYmMxYjRlNGJkMzk1YjM0MTlkZTZlODY1NzkiLCJ1c2VyX2lkIjoyfQ.tzCO2AhmjTqPxo3AYVLkZ-7luDWqntz1dy6zZBmK_0s",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ5ODE3ODMwLCJqdGkiOiJjNThlOGEzNTcwYWY0ZGQ1YjllNjc2ZmRmNjE4MjBhNCIsInVzZXJfaWQiOjJ9.T8K7H_gQ-F5XyipfFlUNAjMCo_TkKbJqoCqQbgIwkNI"
}

{
    "username": "user3",
    "password": "!password123"
}
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0OTgxNzg1NCwianRpIjoiMDBmNDQ5MThjMmQ1NGNkMWI2NDY1MTEyMWI5MGE5ZmQiLCJ1c2VyX2lkIjozfQ.2uYDjr6fBkZ6Rp7iZkS4qYrxz5X94UDz0xtChj-gCWc",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ5ODE3ODU0LCJqdGkiOiI0MTgyNTY0YmRlNTQ0OWYwYmNhZDJmY2ZmZGU0MzNhNyIsInVzZXJfaWQiOjN9.c9A_HukN60ELpxnEG_cxUgw2kpVhwxtC8E2F8_iIvhg"
}
'''