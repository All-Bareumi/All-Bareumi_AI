#-*- coding:utf-8 -*-
import urllib3
import json
import base64
#openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Pronunciation" # 영어
openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/PronunciationKor" # 한국어

accessKey = "MyKey"
audioFilePath = "./data/hayun_wrong_16.wav"
languageCode = "korean"
script = "안녕하세요"

file = open(audioFilePath, "rb")
audioContents = base64.b64encode(file.read()).decode("utf8")
file.close()


def pro_eval():
    requestJson = {   
        "argument": {
            "language_code": languageCode,
            "script": script,
            "audio": audioContents
        }
    }

    http = urllib3.PoolManager()
    response = http.request(
        "POST",
        openApiURL,
        headers={"Content-Type": "application/json; charset=UTF-8","Authorization": accessKey},
        body=json.dumps(requestJson)
    )

    #print("[responseCode] " + str(response.status))
    #print("[responBody]")
    #print(str(response.data,"utf-8"))
    pro_eval_score = json.loads(response.data)["return_object"]["score"]

    return pro_eval_score

if __name__ == "__main__":
    pro_eval()

