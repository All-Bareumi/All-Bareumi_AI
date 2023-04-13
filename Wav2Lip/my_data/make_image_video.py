import cv2

img_path = './elsa.png'
play_time = 195

img = cv2.imread(img_path)

height, width, channels = img.shape

output = cv2.VideoWriter("make_img_video.mp4", cv2.VideoWriter_fourcc(*'MJPG'), 10, (width, height))


for j in range(play_time * 10):  # 10fps 기준으로 계산
    output.write(img)

# 출력 영상 종료
output.release()

