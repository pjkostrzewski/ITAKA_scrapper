from rest_framework.serializers import ModelSerializer, SlugRelatedField
from .models import Offer


class OfferSerializer(ModelSerializer):
    destination = SlugRelatedField(
        read_only=True,
        slug_field='name'
     )

    class Meta:
        model = Offer
        fields = (
            'offer_id',
            'destination',
            'old_price',
            'current_price',
            'rank',
            'link',
            # 'photo',
            # 'date'
        )
