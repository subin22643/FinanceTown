from django.shortcuts import render
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import requests
import urllib.request
import os
import sys
import json

client_id = 'HaZqKzchSa8gsJTIi_El'
client_secret = 'WNqLvGJH0w'
encText = urllib.parse.quote('금융')
URL = 'https://openapi.naver.com/v1/search/news.json?query=' + encText + '&display=100'

@api_view(['GET'])
def news(request):
    request = urllib.request.Request(URL)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        data = json.loads(response_body.decode('utf-8'))
        # '금융'이 제목에 있는 뉴스만 필터링
        filtered_news = [item for item in data['items'] if '금융' in item['title']]
        top_10_news = filtered_news[:10]

        return Response(top_10_news, status=status.HTTP_200_OK)
        # return Response(filtered_news, status=status.HTTP_200_OK)
        # return Response(json.loads(response_body.decode('utf-8')), status=status.HTTP_200_OK)
    else:
        return Response({"message": "조회에 실패했습니다."}, status=status.HTTP_404_NOT_FOUND)