#-*- coding:utf-8 -*-
import urllib3
import json
import scipy.io.wavfile as wav
import numpy as np
import librosa

#openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Pronunciation" # 영어
openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/PronunciationKor" # 한국어

accessKey = ""
audioFilePath = "./data/hayun_wrong_16.wav"
script = "안녕하세요"

def change_sample_rate(input_file, target_sample_rate):
    # 오디오 파일 읽기
    sample_rate, audio = wav.read(input_file)
    
    # 샘플링 주파수 변경
    converted_audio = librosa.resample(audio.astype(float), sample_rate, target_sample_rate)
    
    return converted_audio

def pro_eval(audioFilePath, script):

    languageCode = "korean"

    #file = open(audioFilePath, "rb")
    #audioContents = base64.b64encode(file.read()).decode("utf8")
    #file.close()

    resampling_audio = change_sample_rate(audioFilePath, 16000)

    requestJson = {   
        "argument": {
            "language_code": languageCode,
            "script": script,
            "audio": resampling_audio
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

