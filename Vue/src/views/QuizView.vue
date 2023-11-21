<template>
  <div>
    <h1>웹도리 Quiz</h1>

    <div class="quiz-container">
        <div id="quiz"> </div>  
        <!-- //퀴즈 문제가 들어갈 영역 -->
    </div>

    <div class="quiz-ctrl">
      <button id="previous" class="quiz-btn"> back </button>
      <button id="next" class="quiz-btn"> next </button>
      <button id="submit" class="quiz-btn"> 결과확인 </button>

      <div id="result"> </div> 
      <!-- //퀴즈 결과가 들어갈 영역 -->
    </div>
  </div>
</template>


<script setup>
  const quizData = [
      {
          question : '웹개발에 주로 사용되는 프론트언어는?',
          answers : {
              a : "일본어",
              b : "다랑어",
              c : "자바스크립트"
          },
          correct : 'c'
      },
      {
          question : '웹 디자인에 사용되는 언어는?',
          answers : {
              a : '미싱',
              b : 'css',
              c : '돈까s'
          },
          correct : 'b'
      },
      {
            question : '블로그 형태로 웹사이트를 쉽게 개발할 수 있는 방식을 무엇이라고 하는가?',
            answers : {
                  a : 'CMS',
                  b : 'WAX',
                  c : 'KISWISS'
            },
          correct : 'a'
      }
  ]
  
  const quizDisplay = document.getElementById('quiz');
  const submitBtn = document.getElementById('submit');
  const previousBtn = document.getElementById('previous');
  const nextBtn = document.getElementById('next');

  let currentSlide = 0;
  const resultDisplay = document.getElementById('result');
  
  function buildQuiz(){
        let output = [ ]; 
        quizData.forEach(  
            (currentQuestion, questionNum) => { 
                        const answers = [ ];     
                        for(const item in currentQuestion.answers){  
                                    answers.push(`<label>
                                                  <input type="radio" name="question${questionNum}" value="${item}">
                                                      ${item} : ${currentQuestion.answers[item]}
                                                  </label>`);
                            }
                              output.push(`<div class="slide"><div class="question"> ${currentQuestion.question}</div>
                                            <div class="answer">${answers.join('&nbsp;&nbsp;&nbsp;&nbsp;')}</div></div>`);
                      }              
        );
            quizDisplay.innerHTML = output.join('</br>');
      }
    
  function showResult(){
          const answerDisplays = quizDisplay.querySelectorAll('.answer');  
            let numCorrect = 0; 

              quizData.forEach( (currentQuestion, questionNum)=>{
                    const answerDisplay = answerDisplays[questionNum]; 
                    const selector = `input[name=question${questionNum}]:checked`;  
                    const userAnswer = (answerDisplay.querySelector(selector) || {}).value;  


                      if(userAnswer === currentQuestion.correct){    
                              numCorrect++;
                              answerDisplays[questionNum].style.color = 'lightgreen';
                      }else{
                              answerDisplays[questionNum].style.color = 'red';
                      }
              });
                    
                
                submitBtn.style.display = 'none';
                resultDisplay.innerHTML = `<h3 style="color:#333;">${quizData.length}개중에서 ${numCorrect}개 맞추셨습니다.</h3>`
      }
    
    
  function showSlide(n){
      slides[currentSlide].classList.remove('active-slide');
    slides[n].classList.add('active-slide');
    currentSlide = n;
      if(currentSlide === 0){
          previousBtn.style.display = 'none';
      }else{
          previousBtn.style.display = 'inline-block';
      }
      if(currentSlide === slides.length-1){
          nextBtn.style.display = 'none';
        submitBtn.style.display = 'inline-block';
      }else{
          nextBtn.style.display = 'inline-block';
        submitBtn.style.display = 'none';
                if(document.getElementById('retry')){
                        document.getElementById('retry').style.display = 'none';
                  }
            
      }
  }

  function showNextSlide(){  showSlide(currentSlide+1); }
  function showPreviousSlide(){ showSlide(currentSlide-1); }

  
      buildQuiz(); 
    const slides = document.querySelectorAll('.slide');
    showSlide(currentSlide);
      previousBtn.addEventListener('click',showPreviousSlide);
      nextBtn.addEventListener('click',showNextSlide);
      submitBtn.addEventListener('click',showResult);   
</script>


<style scoped>
.quiz-container{
      position:relative;
      background-color:#f8f6f0;
      font-size:17px;
      color:#333;
      height:150px;
      margin-top:40px;
      text-align:center;
      font-weight:300;
  }
  
  .slide{
     position:absolute;
     left:0px;
     top:40px;
     width:100%;
     z-index:1;
     opacity:0;
     transition:opacity 0.5s;
  }
  
  .active-slide{
     opacity:1;
     z-index:2;
  }
  </style>