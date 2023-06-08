from Pronounce_Evaluation import etri_eval
from Pronounce_Evaluation import my_eval 

import speech_recognition as sr

def eval_main(audioFilePath, script):

    r = sr.Recognizer()
    harvard = sr.AudioFile(audioFilePath)
    with harvard as source:
        audio = r.record(source)
    
    voice_stt = r.recognize_google(audio, language='ko-KR')

    #print("voice_stt ", voice_stt)

    # 0-1
    my_score = my_eval.my_pro_eval(script, voice_stt)
    # 0-5
    etri_score = float(etri_eval.pro_eval(audioFilePath, script))
    # etri_score 정규화
    etri_score /=5

    final_acc = (my_score*0.3 + etri_score*0.7)*5

    return final_acc