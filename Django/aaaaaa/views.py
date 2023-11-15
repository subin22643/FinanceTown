from django.shortcuts import render
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import requests

URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'

@api_view(['GET'])
def exchange(request):
    params = {
        'authkey' : 'Uy013h5RQvCr44y7rRuPpQxSqr2m7TlC',
        # default 값은 오늘날짜인데 원하는 날짜도 입력가능
        'searchdate' : '20231113',
        'data' : 'AP01'
    }
    response = requests.get(URL, params=params).json()
    return JsonResponse({ 'response' : response })