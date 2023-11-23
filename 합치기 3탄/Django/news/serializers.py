from rest_framework import serializers
from .models import Tips

class TipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tips
        fields = '__all__'