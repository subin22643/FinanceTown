from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# 회원간 소통 할 수 있는 커뮤니티 기능(게시판)을 구현합니다.
# • 게시글 조회, 생성, 삭제, 수정 및 댓글 생성, 삭제 기능은 필수로 구현합니다.
# • 회원의 권한에 따라 다른 동작을 하도록 구성합니다.
# • 예시: 본인이 작성한 게시글 및 댓글만 삭제, 수정 가능하도록 구성합니다.
# • 소통 방식은 자유롭게 구성합니다.
# • 예시: 금융 상품 리뷰 게시판, 내가 가입한 상품 자랑 게시판 등


# Create your models here.
class FinanceReview(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_board")
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductReview(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_board")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class QuestionAnswer(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_board")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    finance_review = models.ForeignKey(FinanceReview, on_delete=models.CASCADE, null=True, blank=True)
    product_review = models.ForeignKey(ProductReview, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)