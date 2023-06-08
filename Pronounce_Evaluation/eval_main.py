from etri_eval import pro_eval
from my_eval import my_pro_eval

import speech_recognition as sr

def eval_main(audioFilePath, script):

    r = sr.Recognizer()
    harvard = sr.AudioFile(audioFilePath)
    with harvard as source:
        audio = r.record(source)
    
    voice_stt = r.recognize_google(audio, language='ko-KR')

    #print("voice_stt ", voice_stt)

    # 0-1
    my_score = my_pro_eval(script, voice_stt)
    # 0-5
    etri_score = float(pro_eval(audioFilePath, script))
    # etri_score 정규화
    etri_score /=5

    final_acc = (my_score*0.3 + etri_score*0.7)*5

    return final_acc


audioFilePath = "./fem_correct copy.wav"
script = "안녕하세요"

final_acc = eval_main(audioFilePath, script)
print("final_acc : ", final_acc)
