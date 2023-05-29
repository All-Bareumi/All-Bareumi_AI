import json

# JSON 파일 경로
json_file = '../data/ocr_test.json'

# JSON 파일 읽기
with open(json_file, 'r') as f:
    json_data = json.load(f)

# "inferText" 값 추출
infer_texts = []
for image in json_data['images']:
    for field in image['fields']:
        infer_text = field['inferText']
        infer_texts.append(infer_text)

# 추출된 "inferText" 값 출력
for infer_text in infer_texts:
    print(infer_text)

