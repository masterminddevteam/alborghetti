# coding: utf-8
from django.shortcuts import render
from worker.models import SpiderContent
from .serializers import SpiderSerializer
from rest_framework.response import Response
from rest_framework import authentication, permissions, viewsets
from rest_framework.views import APIView


class SpiderCategoryView(APIView):

    def get(self, request, category):

        queryset = SpiderContent.objects.filter(category=category)
        serializer = SpiderSerializer(queryset, many=True)
        return Response(serializer.data)


class SpiderDetailView(APIView):

    def get(self, request, pk):

        queryset = SpiderContent.objects.filter(pk=pk).last()
        serializer = SpiderSerializer(queryset)
        return Response(serializer.data)