from rest_framework import serializers
from .models import ProductReviews,QuestionAnswers,Comments

class QnASerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswers
        fields = '__all__'
        read_only_fields = ['author','like_users']

class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReviews
        fields = '__all__'
        read_only_fields = ['author','like_users']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        read_only_fields = ['author']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # 외래키 필드가 비어있는 경우, 해당 필드를 Response에서 제외하는 로직
        if not instance.finance_review:
            representation.pop('finance_review', None)
        if not instance.product_review:
            representation.pop('product_review', None)
        return representation
