#-*- coding:utf-8 -*-
import urllib3
import json
import base64
import soundfile as sf
import librosa

#openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Pronunciation" # 영어
openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/PronunciationKor" # 한국어

accessKey = ""
audioFilePath = "./fem_correct.wav"
script = "안녕하세요"


def pro_eval(audioFilePath, script):

    languageCode = "korean"

    audio, sr = librosa.load(audioFilePath, sr=16000)

    sf.write(audioFilePath, audio, 16000)

    file = open(audioFilePath, "rb")
    audioContents = base64.b64encode(file.read()).decode("utf8")
    file.close()


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
    pro_eval_score = pro_eval(audioFilePath, script)
    print(pro_eval_score)

