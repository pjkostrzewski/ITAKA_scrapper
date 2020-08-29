from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Offer


class OfferSerializer(ModelSerializer):
    class Meta:
        model = Offer
        fields = (
            'offer_id',
            'destination',
            'old_price',
            'current_price',
            'rank',
            'link',
            'photo',
            'date'
        )
