from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from datetime import datetime, timedelta
from .serializers import TipsSerializer
import requests
import urllib.request
import json


@api_view(['GET'])
def news(request):
    client_id = 'HaZqKzchSa8gsJTIi_El'
    client_secret = 'WNqLvGJH0w'
    encText = urllib.parse.quote('금융')
    URL = 'https://openapi.naver.com/v1/search/news.json?query=' + encText
    request = urllib.request.Request(URL)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    # if(rescode==200):
    #     response_body = response.read()
    #     print(response_body.decode('utf-8'))
    #     return JsonResponse({ 'response' : response_body.decode('utf-8') })
    # else:
    #     print("Error Code:" + rescode)
    #     return Response({"error": "조회에 실패했습니다"}, status=status.HTTP_404_NOT_FOUND)
    if(rescode==200):
        response_body = response.read()
        return Response(json.loads(response_body.decode('utf-8')), status=status.HTTP_200_OK)
    else:
        return Response({"message": "조회에 실패했습니다."}, status=status.HTTP_404_NOT_FOUND)


def tips(request):
    start_date = datetime(2016, 8, 1)
    end_date = datetime.now()
    one_month = timedelta(days=30)  # 대략적인 한 달 기간

    while start_date < end_date:
        # 한 달 단위로 날짜 설정
        current_end_date = min(start_date + one_month, end_date)
        params = {
            'apiType': 'json',
            'startDate': start_date.strftime('%Y-%m-%d'),
            'endDate': current_end_date.strftime('%Y-%m-%d'),
            'authKey': '489e82582bcb3284d078bbae3e72ca87'
        }
        response = requests.get('https://www.fss.or.kr/fss/kr/openApi/api/tip.jsp', params=params).json()
        if response.status_code == 200:
            serializer = TipsSerializer(response.data)
            if serializer.is_valid():
                serializer.save()
        else:
            # 오류 처리
            print(f"Error with status code {response.status_code} for date range {params['startDate']} to {params['endDate']}")

        # 다음 달로 이동
        start_date = current_end_date

    return JsonResponse({"status": "completed"})