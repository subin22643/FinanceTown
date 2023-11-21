from rest_framework import serializers
from .models import ProductReviews,QuestionAnswers,Comments
from accounts.serializers import CustomDetailSerializer

class QnASerializer(serializers.ModelSerializer):
    author = CustomDetailSerializer(read_only=True)
    liked = serializers.SerializerMethodField() #boardDetail 응답에 좋아요 상태를 반환하기 위함
    likeCount = serializers.SerializerMethodField() #boardDetail 응답에 좋아요 수를 반환하기 위함
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)

    class Meta:
        model = QuestionAnswers
        fields = '__all__'
        read_only_fields = ['author','like_users']

    #hassattr : 객체에 특성 속성이 있으면 True, 없으면 False를 반환하게 해줌. ProductReviewSerializer를 views.py의 prodcuct함수에서도 쓰면서 에러 방지로 사용함.
    def get_liked(self, obj):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            return request.user in obj.like_users.all()
        return False

    # like_users 필드의 사용자 수를 반환
    def get_likeCount(self, obj):
        return obj.like_users.count()

class ProductReviewSerializer(serializers.ModelSerializer):
    author = CustomDetailSerializer(read_only=True)
    liked = serializers.SerializerMethodField() #boardDetail 응답에 좋아요 상태를 반환하기 위함
    likeCount = serializers.SerializerMethodField() #boardDetail 응답에 좋아요 수를 반환하기 위함
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = ProductReviews
        fields = '__all__'
        read_only_fields = ['author', 'like_users']

    #hassattr : 객체에 특성 속성이 있으면 True, 없으면 False를 반환하게 해줌. ProductReviewSerializer를 views.py의 prodcuct함수에서도 쓰면서 에러 방지로 사용함.
    def get_liked(self, obj):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            return request.user in obj.like_users.all()
        return False

    # like_users 필드의 사용자 수를 반환
    def get_likeCount(self, obj):
        return obj.like_users.count()


class CommentSerializer(serializers.ModelSerializer):
    author = CustomDetailSerializer(read_only=True)
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)

    class Meta:
        model = Comments
        fields = '__all__'
        read_only_fields = ['author']