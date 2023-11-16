from rest_framework import serializers
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions

# class DepositProductsSerializer(serializers.ModelSerializer):
#     class Meta():
#         model = DepositProducts
#         fields = '__all__'
        
# class DepositOptionsSerializer(serializers.ModelSerializer):
#     class Meta():
#         model = DepositOptions
#         fields = '__all__'
#         read_only_fields = ('product',)

class DepositProductsSerializer(serializers.ModelSerializer):
    class DepositOptionsSerializer(serializers.ModelSerializer):
        class Meta():
            model = DepositOptions
            fields = '__all__'
    
    deposit_options = DepositOptionsSerializer(read_only=True)
    class Meta():
        model = DepositProducts
        fields = '__all__'
        
class DepositOptionsSerializer(serializers.ModelSerializer):
    product = DepositProductsSerializer(read_only=True)
    class Meta():
        model = DepositOptions
        fields = '__all__'


# class SavingProductsSerializer(serializers.ModelSerializer):
#     class Meta():
#         model = SavingProducts
#         fields = '__all__'
        
# class SavingOptiontsSerializer(serializers.ModelSerializer):
#     class Meta():
        # model = SavingOptions
        # fields = '__all__'
        # read_only_fields = ('product',)


class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta():
        model = SavingProducts
        fields = '__all__'

        
class SavingOptiontsSerializer(serializers.ModelSerializer):
    product = SavingProductsSerializer(read_only=True)
    class Meta():
        model = SavingOptions
        fields = '__all__'