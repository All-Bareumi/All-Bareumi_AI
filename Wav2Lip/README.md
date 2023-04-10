## pth
[link](https://iiitaphyd-my.sharepoint.com/personal/radrabha_m_research_iiit_ac_in/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fradrabha%5Fm%5Fresearch%5Fiiit%5Fac%5Fin%2FDocuments%2FWav2Lip%5FModels%2Fwav2lip%5Fgan%2Epth&parent=%2Fpersonal%2Fradrabha%5Fm%5Fresearch%5Fiiit%5Fac%5Fin%2FDocuments%2FWav2Lip%5FModels&ga=1)
다운로드 후 `checkpoints/` dir에 위치

## Requirements
```code
pip install requirements.txt
```

## Example
```code
python generate_lipsync.py --input_image ./my_data/elsa.png --input_text "엘사야 가자 아렌델로" --gender 0
```
* --input_image: 얼굴 이미지
* --input_text: 생성할 텍스트
* --gender: 0 여성, 1 남성

## Result
최종 결과 파일은 `FINAL` dir 안에 저장됨