from rest_framework import serializers
from .models import FinanceReview,ProductReview,QuestionAnswer

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