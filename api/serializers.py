from rest_framework import serializers
from restaurants.models import Restaurant, Item
from django.contrib.auth.models import User
from django.http import JsonResponse


#In the RestaurantListView to the RestaurantUpdateView.
#In the RestaurantListView to the RestaurantDeleteView.



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'name',
            'description',
            'price'
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]


class RestaurantListSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
    view_name = "api-detail",
    lookup_field = "id",
    lookup_url_kwarg = "restaurant_id"
    )
    update = serializers.HyperlinkedIdentityField(
        view_name = "api-update",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
    )

    delete = serializers.HyperlinkedIdentityField(
        view_name = "api-delete",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
    )
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'opening_time',
            'closing_time',
            'detail',
            'update',
            'delete'
            ]


class RestaurantDetailSerializer(serializers.ModelSerializer):
    update = serializers.HyperlinkedIdentityField(
        view_name = "api-update",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
    )


    delete = serializers.HyperlinkedIdentityField(
        view_name = "api-delete",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
    )

    theowner = serializers.SerializerMethodField()
    theitems = serializers.SerializerMethodField()
    class Meta:
        model = Restaurant
        fields = [
            'id',
            'owner',
            'name',
            'description',
            'opening_time',
            'closing_time',
            'update',
            'delete',
            'theowner',
            'theitems'
            ]

    def get_theowner(self, obj):
        return UserSerializer(obj.owner).data

    def get_theitems(self, obj):
        return ItemSerializer(Item.objects.filter(restaurant = obj), many=True).data
        

class RestaurantCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'description',
            'opening_time',
            'closing_time',
            ]


#In the RestaurantDetailView to the RestaurantUpdateView.
#In the RestaurantDetailView to the RestaurantDeleteView.