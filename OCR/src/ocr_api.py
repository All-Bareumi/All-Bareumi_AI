import requests
import uuid
import time
import json

api_url = 'https://0qx5xa4nma.apigw.ntruss.com/custom/v1/22827/935dda0c23ab575e0046cfd097ae5b9bcc726667c408cf021472ea7373e8d35d/general'
secret_key = ''

def ocr_api(image_file):

    request_json = {
        'images': [
            {
                'format': 'png',
                'name': 'demo'
            }
        ],
        'requestId': str(uuid.uuid4()),
        'version': 'V2',
        'timestamp': int(round(time.time() * 1000))
    }

    payload = {'message': json.dumps(request_json).encode('UTF-8')}
    files = [
    ('file', open(image_file,'rb'))
    ]
    headers = {
    'X-OCR-SECRET': secret_key
    }

    response = requests.request("POST", api_url, headers=headers, data = payload, files = files)

    res = json.loads(response.text.encode('utf8'))
    #print(res)
    json_data = res

    infer_texts = ""
    for image in json_data['images']:
        for field in image['fields']:
            infer_text = field['inferText']
            infer_texts += " "
            infer_texts += infer_text
            #infer_texts.append(infer_text)

    return infer_texts

#check = ocr_api("../data/dongwha.png")
#print(check)