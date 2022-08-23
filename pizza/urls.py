from django.urls import path

from rest_framework_simplejwt import views as jwt_views

from .views import CurrentUserRetrieveAPIView, PizzaListApiView, \
    PizzaCreateApiView, PizzaRetrieveAPIView, DrinkListApiView, \
    DrinkCreateApiView, DrinkRetrieveAPIView, OrderUserRetrieveAPIView, \
    OrderUserCreateApiView, OrderUserListAPIView, \
    IngredientsViewSet, PizzaUpdateAPIView, PizzaDestroyAPIView, DrinkUpdateAPIView, DrinkDestroyAPIView

urlpatterns = [
    path('users/', CurrentUserRetrieveAPIView.as_view()),

    path('ingredient/list/', IngredientsViewSet.as_view({'get': 'list'})),
    path('ingredient/', IngredientsViewSet.as_view({'post': 'create'})),
    path('ingredient/<int:pk>/', IngredientsViewSet.as_view({'get': 'retrieve'})),
    path('ingredient/<int:pk>/update/', IngredientsViewSet.as_view({'put': 'update'})),
    path('ingredient/<int:pk>/delete/', IngredientsViewSet.as_view({'delete': 'destroy'})),

    path('pizza/<int:pk>/', PizzaRetrieveAPIView.as_view()),
    path('pizza/list/', PizzaListApiView.as_view()),
    path('pizza/', PizzaCreateApiView.as_view()),
    path('pizza/<int:pk>/update', PizzaUpdateAPIView.as_view()),
    path('pizza/<int:pk>/delete', PizzaDestroyAPIView.as_view()),

    path('drink/list/', DrinkListApiView.as_view()),
    path('drink/', DrinkCreateApiView.as_view()),
    path('drink/<int:pk>/', DrinkRetrieveAPIView.as_view()),
    path('drink/<int:pk>/update', DrinkUpdateAPIView.as_view()),
    path('drink/<int:pk>/delete', DrinkDestroyAPIView.as_view()),

    path('order/<int:pk>/', OrderUserRetrieveAPIView.as_view()),
    path('order/', OrderUserCreateApiView.as_view()),
    path('order/list/', OrderUserListAPIView.as_view()),

    path('token/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
