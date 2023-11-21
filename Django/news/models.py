from django.db import models

# Create your models here.
class Tips(models.Model):
   contentId= models.CharField  # 컨텐츠의 고유 식별자
   subject= models.CharField  # 내용의 제목
   atchfileNm = models.CharField # 비지니스 규칙 관리 코드
   temp1= models.CharField #임시 필드 1 (여기서는 '은행'으로 지정됨)
   atchfileUrl = models.CharField #첨부 파일의 다운로드 URL
   originUrl = models.CharField #원본 URL (여기서는 비어 있음)
   contentsKor = models.CharField #내용

