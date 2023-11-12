from django.shortcuts import render
from .models import FinanceReview,ProductReview,QuestionAnswer
from .serializers import FinanceReviewSerializer,ProductReviewSerializer,QuestionAnswerSerializer
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

# 회원간 소통 할 수 있는 커뮤니티 기능(게시판)을 구현합니다.
# • 게시글 조회, 생성, 삭제, 수정 및 댓글 생성, 삭제 기능은 필수로 구현합니다.
# • 회원의 권한에 따라 다른 동작을 하도록 구성합니다.
# • 예시: 본인이 작성한 게시글 및 댓글만 삭제, 수정 가능하도록 구성합니다.
# • 소통 방식은 자유롭게 구성합니다.
# • 예시: 금융 상품 리뷰 게시판, 내가 가입한 상품 자랑 게시판 등

@require_http_methods(["GET"])
def boards(request):
    FinanceBoards = FinanceReview.objects.all()
    ProductBoards = ProductReview.objects.all()
    QuestionBoards = QuestionAnswer.objects.all()
    FinanceSerializer = FinanceReviewSerializer(instance=FinanceBoards, many=True)
    ProductSerializer = ProductReviewSerializer(instance=ProductBoards, many=True)
    QuestionSerializer = QuestionAnswerSerializer(instance=QuestionBoards, many=True)

    data = {
        'finance_reviews': FinanceSerializer.data,
        'product_reviews': ProductSerializer.data,
        'question_answers': QuestionSerializer.data,
    }

    return Response(data, status=status.HTTP_200_OK)


# @require_http_methods(["GET", "POST"])
# def detail(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#     like_users = board.like_users.all()

#     if request.method == 'POST':
#         board.delete()
#         return redirect('boards:index')

#     comments= board.comments.all()
#     comment_form = CommentForm()

#     context = {
#         'board': board,
#         'comments': comments,
#         'comment_form': comment_form,
#         'like_users' : like_users,
#     }
#     return render(request, 'boards/detail.html', context)


# @login_required
# @require_http_methods(["GET", "POST"])
# def update(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#     if request.user == board.author:
#         if request.method == 'POST':
#                 form = BoardForm(request.POST, instance=board)
#                 if form.is_valid():
#                     form.save()
#                     return redirect('boards:detail', board.pk)
#         else:
#             form = BoardForm(instance=board)
#         context = {
#             'board': board,
#             'form': form,
#         }
#         return render(request, 'boards/update.html', context)


# @login_required
# @require_http_methods(["GET", "POST"])
# def create(request):
#     if request.method == 'POST':
#         form = BoardForm(request.POST)
#         if form.is_valid():
#             board = form.save(commit=False)
#             board.author = request.user
#             form.save()
#             return redirect('boards:index')
#     else:
#         form = BoardForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'boards/create.html', context)


# @login_required
# @require_http_methods(["POST"])
# def comment(request, board_pk):
#     board = get_object_or_404(Board, pk=board_pk)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.board = board
#             comment.author = request.user
#             comment.save()
#             return redirect('boards:detail', board.pk)


# @require_http_methods(["POST"])
# def comment_delete(request, board_pk, comment_pk):
#     comment = get_object_or_404(Comment, pk=comment_pk)
#     if request.user == comment.author:
#         if request.method == 'POST':
#             comment.delete()
#             return redirect('boards:detail', board_pk)
        

# @require_POST
# def like_articles(request,pk):
#     board = Board.objects.get(pk=pk)
#     me = request.user

#     if me in board.like_users.all():
#         board.like_users.remove(me)
#     else:
#         board.like_users.add(me)

#     return redirect('boards:detail', pk)