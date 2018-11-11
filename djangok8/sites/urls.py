"""djangok8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http import Http404
from django.urls import path, include
from rest_framework import serializers, viewsets, routers, status
from rest_framework.response import Response
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.views import APIView

from djangok8.sites.models import Site


class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = ('url', 'id', 'status','status_code', 'last_check_at', 'site_url')




class SiteList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    serializer_class = SiteSerializer

    def get(self, request, format=None):
        snippets = Site.objects.all()
        serializer = SiteSerializer(snippets, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SiteSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SiteDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    serializer_class = SiteSerializer
    def get_object(self, pk):
        try:
            return Site.objects.get(pk=pk)
        except Site.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SiteSerializer(snippet, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SiteSerializer(snippet, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, pk, req):
        site = self.get_object(pk)
        site.update_availability()

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

urlpatterns = [
    # url(r'^', include(router.urls)),
    path('sites/', SiteList.as_view()),
    path('site/<pk>/', SiteDetail.as_view(), name='site-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)

