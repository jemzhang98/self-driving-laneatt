import os
import cv2

dirname = 'output-temp-2022-04-01_15-33-33-front.mp4'
image_folder = 'C:/Users/jzhan/OneDrive/Documents/GitHub/LaneATT/datasets/tesla-test/' + dirname
vid_out_path = 'C:/Users/jzhan/OneDrive/Documents/GitHub/LaneATT/datasets/tesla-test/output-video/'
vid_name = dirname


cap = cv2.VideoCapture(0)

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape
fourc = cv2.VideoWriter_fourcc(*'MP4V')
video = cv2.VideoWriter(vid_out_path + vid_name, fourc, 20, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()
