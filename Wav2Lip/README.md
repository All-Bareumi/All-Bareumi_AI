## pth
[link](https://iiitaphyd-my.sharepoint.com/personal/radrabha_m_research_iiit_ac_in/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fradrabha%5Fm%5Fresearch%5Fiiit%5Fac%5Fin%2FDocuments%2FWav2Lip%5FModels%2Fwav2lip%5Fgan%2Epth&parent=%2Fpersonal%2Fradrabha%5Fm%5Fresearch%5Fiiit%5Fac%5Fin%2FDocuments%2FWav2Lip%5FModels&ga=1)
다운로드 후 `checkpoints/` dir에 위치시킨다

## Requirements
```code
pip install requirements.txt
```
* If needed(maybe window os)
```code
conda install ffmpeg
```

## Example
```code
python generate_lipsync.py --input_image ./my_data/elsa.png --input_text "안나야 가자 아렌델로" --gender 0
```
* --input_image: 얼굴 이미지
* --input_text: 생성할 텍스트
* --gender: 0 여성, 1 남성

## Result
* 최종 결과 파일은 `FINAL` dir 안에 저장됨
* `generate_lipsync.py` 의 main 함수 return 값은 영상이 저장된 경로(str)
    * output string ex) /FINAL/elsa/안나야_가자_아렌델로.mp4

## 예문 리스트(230411)
* File: [FINAL.zip](./FINAL/FINAL.zip)
    * 캐릭터: 엘사, 안나, 크리스토프, 한스

<img src="./my_data/anna.png" width="22%">
<img src="./my_data/elsa.png" width="22%">
<img src="./my_data/kristoff.png" width="22%">
<img src="./my_data/hans.png" width="22%">


### 음식 관련
1. 내가 제일 좋아하는 과일은 수박이에요  
2. 나는 엄마랑 밥을 먹을 때 가장 행복해요  
3. 나는 초콜릿과 사탕을 매우 좋아해요  
4. 나는 피자와 핫도그를 좋아해요  
5. 오늘 점심에는 치킨 너겟과 감자 튀김을 먹을 거예요  

### 운동 관련
1. 나는 놀이공원에서 롤러코스터를 탈 거예요  
2. 나는 자전거를 타고 주변을 돌아다니면서 신나게 운동해요  
3. 오늘 유치원에서 달리기를 했어요  
4. 친구들과 축구를 하면 기분이 좋아져요  
5. 나는 달리기를 잘해요  

### 가족 관련
1. 내가 가장 사랑하는 건 가족이에요  
2. 엄마는 나를 사랑하세요  
3. 아빠는 정말 멋있어요  
4. 우리 가족은 다섯 명이에요  
5. 저녁은 매일 가족들과 먹어요  

### 학교 관련
1. 나는 학교에 가는 게 재미있어요  
2. 학교에 가면 친구들과 선생님이 있어요  
3. 우리 학교에는 도서관이 있어요  
4. 내일은 학교에 가는 날이에요  
5. 친구들과 먹는 급식은 맛있어요  


---
## ISSUE
#### 음성 인식(Speech to Text) 관련
* SpeechRecognition 라이브러리 사용
    * 음성을 너무 정확하게 인식함(발음이 뭉게지더라도 보정이 됨)
#### 발음 분석 관련
* 단순 정확도 계산: 전체 글자 중 몇 개를 맞췄는지
<img src="./img/hi.png" width="22%">
    * 1:1 비교가 어려움
* Ground Truth 음성의 mel-spectrogram과 유사도 비교
    * 이미지 -> Histogram
    * cos 유사도
    * 특징점 비교(SHIFT)
    * 특성 매칭(FLANN(Fast Library for Approximate Nearest Neighbors))

