from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.conf import settings
from django.http import JsonResponse
import requests
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer, SavingProductsSerializer, SavingOptiontsSerializer


# @@@@@@@@@@@@ params에 pageNO 수정 해야함
BASE_URL = 'https://finlife.fss.or.kr/finlifeapi/'
DEPOSIT_URL = BASE_URL + 'depositProductsSearch.json'
SAVING_URL = BASE_URL + 'savingProductsSearch.json'
params = {
    'auth': settings.SEARCH_API_KEY,
    'topFinGrpNo': '020000',
    'pageNo': '1',
    }

# BASE_URL = 'https://www.fss.or.kr/fss/kr/openApi/api/tip.jsp?'
# params = {
#     'apiType' : 'json',
#     'startDate': '',
#     'endDate': '',
#     'authKey': '1',
#     }

@api_view(['get'])
def deposit_index(request):
    products = DepositProducts.objects.all()
    serializer = DepositProductsSerializer(products, many = True)
    return Response({ 'response': serializer.data })

    
# 특정 상품의 옵션 조회하면 상품 데이터도 반환
@api_view(['GET'])
def deposit_products_options(request, fin_prdt_cd):
    try:
        product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    except DepositProducts.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = DepositProductsSerializer(product)
    return Response(serializer.data)


@api_view(['get'])
def saving_index(request):
    products = SavingProducts.objects.all()
    serializer = SavingProductsSerializer(products, many = True)
    return Response({ 'response': serializer.data })


# 특정 상품 데이터랑 옵션 리스트 같이 반환 
@api_view(['GET'])
def saving_products_options(request, fin_prdt_cd):
    try:
        product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    except SavingProducts.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = SavingProductsSerializer(product)
    return Response(serializer.data)


# requests 모듈을 활용하여
# 정기예금 상품 목록 데이터를 가져와
# 정기예금 상품 목록, 옵션 목록을 DB에 저장
@api_view(['GET'])
def save_deposit_products(request):
    response = requests.get(DEPOSIT_URL, params=params).json()
    products = response['result']['baseList']
    options = response['result']['optionList']

    for product in products:
        serializer = DepositProductsSerializer(data=product)
        #'save-deposit-products/'을 들어갈 떄마다 DB에 저장을 해야되는데 fin_prdt_cd가 unique로 되어 있어서 에러가 뜸
        # unique 안되어 있으면 새로고침이나 url로 들어갈때마다 중복자료 계속 저장됨
        # 해당 데이터를 처리하기 위해 try, except 사용 → 그냥 raise_exception =True를 안하면 try,except 없이 해도 되긴함
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        except ValidationError:
            continue


    for option in options:
        try:
            product = DepositProducts.objects.get(fin_prdt_cd=option['fin_prdt_cd'])
            serializer =DepositOptionsSerializer(data=option)
            if serializer.is_valid(raise_exception=True):
                serializer.save(product=product)
        except DepositProducts.DoesNotExist: #get에서 일치하는 정보가 없을 경우
            continue        
        except ValidationError:
            continue

    return Response({"message": "성공적으로 처리되었습니다."},status=status.HTTP_201_CREATED)


# requests 모듈을 활용하여
# 정기예금 상품 목록 데이터를 가져와
# 정기예금 상품 목록, 옵션 목록을 DB에 저장
@api_view(['GET'])
def save_saving_products(request):
    response = requests.get(SAVING_URL, params=params).json()
    products = response['result']['baseList']
    options = response['result']['optionList']

    for product in products:
        serializer = SavingProductsSerializer(data=product)
        #'save-deposit-products/'을 들어갈 떄마다 DB에 저장을 해야되는데 fin_prdt_cd가 unique로 되어 있어서 에러가 뜸
        # unique 안되어 있으면 새로고침이나 url로 들어갈때마다 중복자료 계속 저장됨
        # 해당 데이터를 처리하기 위해 try, except 사용 → 그냥 raise_exception =True를 안하면 try,except 없이 해도 되긴함
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        except ValidationError:
            continue

    for option in options:
        try:
            product = SavingProducts.objects.get(fin_prdt_cd=option['fin_prdt_cd'])
            serializer =SavingOptiontsSerializer(data=option)
            if serializer.is_valid(raise_exception=True):
                serializer.save(product=product)
        except SavingProducts.DoesNotExist: #get에서 일치하는 정보가 없을 경우
            continue        
        except ValidationError:
            continue
    
    return JsonResponse({ "message": "okay"})




# # 특정 상품의 옵션 조회하면 상품 데이터도 반환
# @api_view(['GET'])
# def deposit_products_options(request, fin_prdt_cd):
#     product = DepositProducts.objects.get(fin_prdt_cd = fin_prdt_cd)
#     option = product.deposit_options.all()
#     serializer = DepositOptionsSerializer(option=option, many = True)
#     return Response(serializer.data)


# 특정 상품 데이터 조회하면 옵션도 같이 반환
@api_view(['GET'])
def deposit_product(request, fin_prdt_cd):
    product = DepositProducts.objects.get(fin_prdt_cd = fin_prdt_cd)
    option = product.deposit_options.all()
    serializer = DepositOptionsSerializer(option, many = True)
    return Response(serializer.data)





# 가입 기간에 상관없이
# 금리가 가장 높은 상품과 해당 상품의 옵션 리스트 출력
@api_view(['GET'])
def top_rate_deposit(request):
    options = DepositOptions.objects.all()
    rates = []
    for option in options:
        rates.append(option.intr_rate2)
    max_rate = max(rates)

    top_options = DepositOptions.objects.filter(intr_rate2=max_rate)
    prdt_cd = []
    for option in top_options:
        prdt_cd.append(option.fin_prdt_cd)
    products = DepositProducts.objects.filter(fin_prdt_cd__in = prdt_cd)
    data = {
        "deposit_product": DepositProductsSerializer(products, many=True).data,
        "options": DepositOptionsSerializer(top_options, many=True).data,
    }
    
    return Response(data)


# 가입 기간에 상관없이
# 금리가 가장 높은 상품과 해당 상품의 옵션 리스트 출력
@api_view(['GET'])
def top_rate_saving(request):
    options = SavingOptions.objects.all()
    rates = []
    for option in options:
        rates.append(option.intr_rate2)
    max_rate = max(rates)

    top_options = SavingOptions.objects.filter(intr_rate2=max_rate)
    prdt_cd = []
    for option in top_options:
        prdt_cd.append(option.fin_prdt_cd)
    products = SavingProducts.objects.filter(fin_prdt_cd__in = prdt_cd)
    data = {
        "deposit_product": SavingProductsSerializer(products, many=True).data,
        "options": SavingOptiontsSerializer(top_options, many=True).data,
    }
    
    return Response(data)