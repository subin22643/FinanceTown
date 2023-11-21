from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from datetime import datetime
from .serializers import TipsSerializer
from .models import Tips
import requests
import urllib.request
import json
from pprint import pprint


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

@api_view(['GET'])
def tips(request):
    if Tips.objects.exists():  # DB에 데이터가 이미 있는 경우
      data = Tips.objects.all() 
      return Response({"data": "data"})
    
    else:
      start_date = datetime(2016, 8, 1)
      end_date = datetime.now()
      params = {
          'apiType': 'json',
          'startDate': start_date.strftime('%Y-%m-%d'),
          'endDate': end_date.strftime('%Y-%m-%d'),
          'authKey': '489e82582bcb3284d078bbae3e72ca87'
      }
      response = requests.get('https://www.fss.or.kr/fss/kr/openApi/api/tip.jsp', params=params).json()

      # response 데이터 까보고 key, value 잘 찾아서 실험하기, api 요청 하루 30번 가능함
      results = response.get('reponse', {}).get('result', [])

      response_str = json.dumps(response, ensure_ascii=False, indent=4)
      with open('response.txt','w',encoding='utf-8') as file:
          file.write(response_str)

      for result in results:
          # 각 결과를 모델 인스턴스로 변환하고 저장
          serializer = TipsSerializer(data=result)
          if serializer.is_valid():
              serializer.save()
          else:
              print(f"Validation failed for data: {result}")

    return Response({"status": "completed"})