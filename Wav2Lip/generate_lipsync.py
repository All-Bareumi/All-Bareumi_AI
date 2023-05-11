import argparse
import os
import math

from navertts import NaverTTS
from gtts import gTTS
from mutagen.mp3 import MP3
import cv2
import subprocess
import platform


"""parsing and configuration"""
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_image', type=str, required=True, help='target image path')
    parser.add_argument('--input_text', type=str, required=True, help='text what you want to generate')
    parser.add_argument('--gender', type=int, default='0', help='0 woman 1 man')

    return check_args(parser.parse_args())

"""checking arguments"""
def check_args(args):
    os.path.isfile(args.input_image)
    try:
        assert os.path.isfile(args.input_image)
    except:
        print("There's no file")
    return args

"""main"""
def main():
    # parse arguments
    args = parse_args()
    if not os.path.isdir('./TTS'):
        os.mkdir('./TTS')
    if not os.path.isdir('./img2video'):
        os.mkdir('./img2video')
    if not os.path.isdir('./FINAL'):
        os.mkdir('./FINAL')

    # 여성이면
    if not args.gender:
        tts = NaverTTS(args.input_text)
        tts.save('./TTS/'+args.input_text.replace(' ','_')+'.wav')
    # 남성이면
    else:
        tts = gTTS(text=args.input_text, lang='ko')
        tts.save('./TTS/'+args.input_text.replace(' ','_')+'.wav')

    # input 이미지로 음성파일과 duration 같은 영상 만들기
    

    audio = MP3('./TTS/'+args.input_text.replace(' ','_')+'.wav')

    duration = math.ceil(audio.info.length)
    img = cv2.imread(args.input_image)
    height, width, channels = img.shape
    output = cv2.VideoWriter("./img2video/"+args.input_text.replace(' ','_')+".mp4", cv2.VideoWriter_fourcc(*'MJPG'), 10, (width, height))

    for j in range(duration * 10):  # 10fps 기준으로 계산
        output.write(img)
    output.release()

    face = "./img2video/"+args.input_image.split('.')[0]+args.input_text.replace(' ','_')+".mp4"
    audio = './TTS/'+args.input_text.replace(' ','_')+'.wav'
    outfile = './FINAL/'+args.input_image.split('/')[2].split('.')[0]+'/'+args.input_text.replace(' ','_')+".mp4"

    if not os.path.isdir('./FINAL/'+args.input_image.split('/')[2].split('.')[0]):
        os.mkdir('./FINAL/'+args.input_image.split('/')[2].split('.')[0])

    # 위에서 만든 TTS 파일 + 이미지 영상 파일 합성하여 립싱크 모델 생성
    string = 'python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face ' + face +' --audio '+ audio +' --outfile ' + outfile
    subprocess.call(string, shell=platform.system() != 'Windows')

    return outfile


if __name__ == "__main__":
	main()

# python generate_lipsync.py --input_image ./my_data/hans.png --input_text "내가 제일 좋아하는 과일은 수박이란다" --gender 1
# python generate_lipsync.py --input_image ./my_data/kristoff.png --input_text "내가 제일 좋아하는 과일은 수박이에요" --gender 1