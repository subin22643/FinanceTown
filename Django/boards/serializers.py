from rest_framework import serializers
from .models import FinanceReview,ProductReview,QuestionAnswer,Comment

class FinanceReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceReview
        fields = '__all__'

class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'

class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # 외래키 필드가 비어있는 경우, 해당 필드를 Response에서 제외하는 로직
        if not instance.finance_review:
            representation.pop('finance_review', None)
        if not instance.product_review:
            representation.pop('product_review', None)
        return representation

