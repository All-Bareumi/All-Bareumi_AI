# All-Bareumi_AI
DL Code / Flask BE server


---
## Wav2Lip
* pre-trained model은 사람 얼굴을 대상으로 학습된 모델이라 애니메이션 얼굴에 적용했을 때 어색함이 있음
* 해결 방안: 애니메이션에 대한 데이터를 추가하여 transfer-learning
    * 애니메이션 데이터 구축 방안
        1. 영상(SLR2) 불러와서 소리/영상 분리하고 프레임 추출
        2. 프레임 각각 인공지능 돌려서 style transfer
        3. 프레임 이어붙여서 영상으로 제작
        4. 소리와 합성하여 저장
    * 문제점
        * U-GOT-IT: pre-trained model이 없어 바닥부터 학습해야 하고, 다른 사람들이 만들어놓은 가중치로 실험했을 때 성능이 좋지 않았음
        * CartoonGAN: pre-trained model이 있긴 하나 결과 확인해보았을 때 애니메이션보다는 수채화 느낌 + 기대한 만큼의 성능 안나옴
        * AnimeGANv2: 성능은 가장 좋으나 결과를 보면 뭉게지는 경향이 있음
        * 공통적으로 style transfer 모델이 모두 입모양을 제대로 볼 수 있을 만큼 정교하지 않음
        * SLR2 데이터 확보 문제: 지도 교수의 승인 필요

#### Wav2Lip
* pre-trained 모델 load 후 test 완료
* 한국어 fine-tunning 전
* local 작업 시 librosa install 이슈
#### Text To Speech
gTTS  
* python 음성 모듈
* 영어 - 여성 성우, 한국어 - 남성 성우 (변경 불가)

Kakao 음성 API  
* STT와 TTS 제공
* 목소리, 발화 속도, 볼륨 조절, 목소리 사이 break time 등 다양한 옵션 제공
* General TTS는 1,000,000자 이하까지 1자 당 0.072원

Clova 음성 API  
* 서비스 종료
* Unofficial python api가 있으며, 여성 성우

## OCR


## Pronounce Analysis

