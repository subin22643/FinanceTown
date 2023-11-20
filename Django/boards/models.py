from django.db import models
from django.conf import settings


# 회원간 소통 할 수 있는 커뮤니티 기능(게시판)을 구현합니다.
# • 게시글 조회, 생성, 삭제, 수정 및 댓글 생성, 삭제 기능은 필수로 구현합니다.
# • 회원의 권한에 따라 다른 동작을 하도록 구성합니다.
# • 예시: 본인이 작성한 게시글 및 댓글만 삭제, 수정 가능하도록 구성합니다.
# • 소통 방식은 자유롭게 구성합니다.
# • 예시: 금융 상품 리뷰 게시판, 상담 게시판 등


# Create your models here.
class ProductReviews(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_product")
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class QuestionAnswers(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_QnA")
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comments(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductReviews, on_delete=models.CASCADE, null=True, blank=True, related_name="product_comments")
    QnA = models.ForeignKey(QuestionAnswers, on_delete=models.CASCADE, null=True, blank=True, related_name="QnA_comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)