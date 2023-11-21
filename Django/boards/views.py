from django.shortcuts import render,get_object_or_404,get_list_or_404
from .models import ProductReviews,QuestionAnswers,Comments
from .serializers import ProductReviewSerializer,QnASerializer,CommentSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

# Create your views here.
# 회원간 소통 할 수 있는 커뮤니티 기능(게시판)을 구현합니다.
# • 게시글 조회, 생성, 삭제, 수정 및 댓글 생성, 삭제 기능은 필수로 구현합니다.
# • 회원의 권한에 따라 다른 동작을 하도록 구성합니다.
# • 예시: 본인이 작성한 게시글 및 댓글만 삭제, 수정 가능하도록 구성합니다.
# • 소통 방식은 자유롭게 구성합니다.
# • 예시: 금융 상품 리뷰 게시판, 내가 가입한 상품 자랑 게시판 등
# 각 게시판 종류별 전체 조회/생성 + 단일 게시판 조회/수정/삭제 구현


#@@@@@@@@@@@@@@@@@@@@@@@게시판 종류별 전체 조회/생성 + 단일 게시판 상세 조회/수정/삭제 구현 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def product(request):
    if request.method == 'GET':
        productBoards = ProductReviews.objects.all().order_by('-created_at')
        serializer = ProductReviewSerializer(productBoards, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def product_detail(request, product_pk):
    productBoard = get_object_or_404(ProductReviews, pk=product_pk)

    if request.method == 'GET':
        serializer = ProductReviewSerializer(productBoard)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProductReviewSerializer(productBoard, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author = request.user)
            return Response(serializer.data)

    elif request.method == 'DELETE':
        productBoard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def QnA(request):
    if request.method == 'GET':
        QnABoards = QuestionAnswers.objects.all().order_by('-created_at')
        serializer = QnASerializer(QnABoards, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QnASerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 필요한 데코레이터 추가하기
@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def QnA_detail(request, QnA_pk):
    QnABoard = get_object_or_404(QuestionAnswers, pk=QnA_pk)

    if request.method == 'GET':
        serializer = QnASerializer(QnABoard)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = QnASerializer(QnABoard, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author = request.user)
            return Response(serializer.data)
        
    elif request.method == 'DELETE':
        QnABoard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#@@@@@@@@@@@@@@@@@@@@@@좋아요 기능 구현@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def product_like(request, product_pk):
    productBoard = get_object_or_404(ProductReviews, pk=product_pk)

    if request.user in productBoard.like_users.all():
        productBoard.like_users.remove(request.user)
    else:
        productBoard.like_users.add(request.user)

    productBoard.save()
    return Response({'status': 'ok'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def QnA_like(request, QnA_pk):
    QnABoard = get_object_or_404(QuestionAnswers, pk=QnA_pk)

    if request.user in QnABoard.like_users.all():
        QnABoard.like_users.remove(request.user)
    else:
        QnABoard.like_users.add(request.user)

    QnABoard.save()
    return Response({'status': 'ok'})


#@@@@@@@@@@@@@@@@@@@@@@댓글 구현@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@api_view(['GET','PUT', 'POST'])
@permission_classes([IsAuthenticated])
def product_comments(request, product_pk):
    product = get_object_or_404(ProductReviews,pk=product_pk)
    if request.method == 'GET':
        comments = product.product_comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


    elif request.method == 'PUT':
        comment_id = request.GET.get('commentId')
        comment = get_object_or_404(Comments, pk=comment_id)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, product=product)
            return Response(serializer.data)
        

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# 댓글 삭제
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def product_comments_delete(request, comment_pk):
    if request.method == 'DELETE':
        comment = get_object_or_404(Comments, pk=comment_pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','PUT', 'POST','DELETE'])
@permission_classes([IsAuthenticated])
def QnA_comments(request, QnA_pk):
    QnA = get_object_or_404(QuestionAnswers,pk=QnA_pk)
    if request.method == 'GET':
        comments = QnA.QnA_comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        comment_id = request.GET.get('commentId')
        comment = get_object_or_404(Comments, pk=comment_id)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, QnA=QnA)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, QnA=QnA)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
# 댓글 삭제
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def QnA_comments_delete(request, comment_pk):
    if request.method == 'DELETE':
        comment = get_object_or_404(Comments, pk=comment_pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comments_detail(request, comment_pk):
    comment = get_object_or_404(Comments, pk=comment_pk)

    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)