from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, exceptions
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .models import Offer
from .serializers import OfferSerializer
from datetime import datetime
import pytz


class OfferList(APIView):
    def get(self, request):
        offers = Offer.objects.all()
        serializer = OfferSerializer(offers, many=True)
        return Response(serializer.data)


class OfferListApiView(ListAPIView):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()

    filter_fields = (
        'destination',
    )
    search_fields = (
        'destination',
    )


class OfferViewSet(ModelViewSet):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()
    filter_fields = ('destination', )
    search_fields = ('destination', )