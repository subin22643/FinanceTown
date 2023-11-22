# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz,QuizRecord
from .serializers import QuizSerializer
from django.utils import timezone


@api_view(['GET','POST'])
def quiz(request):
    if request.method == "GET":
        today = timezone.now().date()
        user_id = request.user.id
        print(user_id)
        print(today)
        already_answered = QuizRecord.objects.filter(user_id=user_id, date_answered=today).exists()
        print(QuizRecord.objects.filter(user_id=user_id, date_answered=today))
        print(already_answered)
        # quizzes = Quiz.objects.all()
        # serializer = QuizSerializer(quizzes, many=True)

         # 랜덤으로 하나의 퀴즈를 선택합니다.
        quiz = Quiz.objects.order_by('?').first()
        serializer = QuizSerializer(quiz)  # 한 개의 퀴즈만 직렬화합니다.
        
        return Response({
            'quizzes': serializer.data,
            'alreadyAnswered': already_answered
        })
    
    if request.method == "POST":
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def alreadyQuiz(request):
  if request.method == 'POST':
        # 사용자가 퀴즈에 답변을 제출했을 때의 로직
        user = request.user
        quiz_id = request.data.get('quiz_id')
        quiz = Quiz.objects.get(pk=quiz_id)
        QuizRecord.objects.create(user=user, quiz=quiz, date_answered=timezone.now().date())

        return Response(status=status.HTTP_201_CREATED)