from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from datetime import datetime, timedelta
from .serializers import TipsSerializer
from .models import Tips
import requests
import urllib.request
import json


@api_view(['GET'])
def news(request):
    client_id = settings.NEWS_ID
    client_secret = settings.NEWS_SECRET
    encText = urllib.parse.quote('금융')
    URL = 'https://openapi.naver.com/v1/search/news.json?query=' + encText + '&display=100'
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
    

@api_view(['GET'])
def tips(request):
    if Tips.objects.exists():  # DB에 데이터가 이미 있는 경우
      datas = Tips.objects.all().order_by('?')[:10]
      serializer = TipsSerializer(datas, many=True)
      return Response({ 'data': serializer.data })
    
    else:
        # # 조회기간이 1개월 단위이고, API 횟수가 30번이라 dB저장시 start,end_date 바꿔가면서 노가다하기
        end_date = datetime.now()
        start_date = end_date.replace(day=1)
        while start_date > datetime(2016, 6, 1):

            params = {
                'apiType': 'json',
                'startDate': start_date.strftime('%Y-%m-%d'),
                'endDate': end_date.strftime('%Y-%m-%d'),
                'authKey': settings.TIPS_API_KEY
            }

            response = requests.get('https://www.fss.or.kr/fss/kr/openApi/api/tip.jsp', params=params).json()
            results = response['reponse']['result']

            # 결과 처리 및 데이터베이스 저장
            for result in results:
                serializer = TipsSerializer(data=result)
                print(result)
                if serializer.is_valid():
                    serializer.save()

            # 다음 달로 날짜 업데이트
            end_date = start_date - timedelta(days=1)
            start_date = end_date.replace(day=1)

        return Response({"status": "completed"})