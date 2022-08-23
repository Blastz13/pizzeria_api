from rest_framework import permissions
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import IngredientPizza, Pizza, Drink, OrderUser
from .permissions import IsOwner
from .serializers import UserDetailInfoSerializer, IngredientPizzaSerializer, \
                         PizzaSerializer, PizzaCreateSerializer, \
                         DrinkSerializer, OrderUserSerializer, \
                         OrderUserCreateSerializer


class CurrentUserRetrieveAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserDetailInfoSerializer(request.user)
        return Response(serializer.data)


class IngredientsViewSet(ModelViewSet):
    queryset = IngredientPizza.objects.all()
    serializer_class = IngredientPizzaSerializer
    permission_classes = [IsAuthenticated]


class PizzaListApiView(generics.ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaCreateApiView(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = PizzaCreateSerializer


class PizzaUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = PizzaCreateSerializer
    queryset = IngredientPizza.objects.all()


class PizzaDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = IngredientPizza.objects.all()


class PizzaRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()


class DrinkListApiView(generics.ListAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer


class DrinkCreateApiView(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = DrinkSerializer


class DrinkRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = DrinkSerializer
    queryset = Drink.objects.all()


class DrinkUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = DrinkSerializer
    queryset = Drink.objects.all()


class DrinkDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Drink.objects.all()


class OrderUserRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsOwner]
    serializer_class = OrderUserSerializer
    queryset = OrderUser.objects.all()


class OrderUserCreateApiView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderUserCreateSerializer

    def perform_create(self, serializer):
        serializer.save(self.request.user)


class OrderUserListAPIView(generics.ListAPIView):
    permission_classes = [IsOwner]
    serializer_class = OrderUserCreateSerializer

    def get_queryset(self):
        return OrderUser.objects.filter(owner_id=self.request.user)
