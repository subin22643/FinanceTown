from django.db import models

class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True) # 금융상품 코드
    fin_co_no = models.TextField(null=True) # 금융 회사 코드
    kor_co_nm = models.TextField()  # 금융 회사명
    fin_prdt_nm = models.TextField()  # 금융 상품명
    mtrt_int = models.TextField(null=True) # 만기 후 이자율
    etc_note = models.TextField()  # 금융 상품 설명
    join_deny = models.IntegerField()  # 가입 제한 (1:제한없음, 2:서민전용, 3:일부제한)
    join_member = models.TextField()  # 가입대상
    join_way = models.TextField()  # 가입 방법
    spcl_cnd = models.TextField()  # 우대 조건
    max_limit = models.TextField(null=True) # 최고 한도
    etc_note = models.TextField() # 기타 유의사항
    dcls_month = models.TextField(null=True) # 공시 제출월 [YYYYMM]
    dcls_strt_daymit = models.TextField(null=True) # 공시 시작일
    dcls_end_day = models.TextField(null=True) # 공시 종료일
    fin_co_subm_day = models.TextField(null=True) # 금융회사 제출일 [YYYYMMDDHH24MI]


class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE, related_name='deposit_options')
    fin_prdt_cd = models.TextField()    # 금융 상품 코드
    intr_rate_type = models.TextField(null=True) # 저축 금리 유형
    intr_rate_type_nm = models.CharField(max_length=100)  # 저축금리 유형명
    intr_rate = models.FloatField(null=True, default=-1)  # 저축금리
    intr_rate2 = models.FloatField(null=True, default=-1)     # 최고 우대 금리
    save_trm = models.IntegerField()   # 저축기간 (단위:개월)


class SavingProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True) # 금융상품 코드
    fin_co_no = models.TextField(null=True) # 금융 회사 코드
    kor_co_nm = models.TextField()  # 금융 회사명
    fin_prdt_nm = models.TextField()  # 금융 상품명
    mtrt_int = models.TextField(null=True) # 만기 후 이자율
    etc_note = models.TextField()  # 금융 상품 설명
    join_deny = models.IntegerField()  # 가입 제한 (1:제한없음, 2:서민전용, 3:일부제한)
    join_member = models.TextField()  # 가입대상
    join_way = models.TextField()  # 가입 방법
    spcl_cnd = models.TextField()  # 우대 조건
    max_limit = models.TextField(null=True) # 최고 한도
    etc_note = models.TextField() # 기타 유의사항
    dcls_month = models.TextField(null=True) # 공시 제출월 [YYYYMM]
    dcls_strt_daymit = models.TextField(null=True) # 공시 시작일
    dcls_end_day = models.TextField(null=True) # 공시 종료일
    fin_co_subm_day = models.TextField(null=True) # 금융회사 제출일 [YYYYMMDDHH24MI]


class SavingOptions(models.Model):
    product = models.ForeignKey(SavingProducts, on_delete=models.CASCADE, related_name='saving_options')
    fin_prdt_cd = models.TextField()    # 금융 상품 코드
    intr_rate_type = models.TextField(null=True, default=-1) # 저축 금리 유형
    intr_rate_type_nm = models.CharField(max_length=100)  # 저축금리 유형명
    rsrv_type = models.TextField # 적립 유형
    rsrv_type_nm = models.TextField # 적립 유형명
    intr_rate = models.FloatField(null=True, default=-1)  # 저축금리
    intr_rate2 = models.FloatField(null=True, default=-1)     # 최고 우대 금리
    save_trm = models.IntegerField()   # 저축기간 (단위:개월)

