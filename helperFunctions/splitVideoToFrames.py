import os
import cv2


dir_name = "C:/Users/jzhan/OneDrive/Documents/GitHub/LaneATT/datasets/tesla-test/input/"
filenames = []
for (_, _, filename) in os.walk(dir_name):
  filenames += filename

for vidname in filenames:
  dirpath = dir_name + vidname
  total_frames = 0
  cap = cv2.VideoCapture(dirpath)
  count = 0
  while cap.isOpened():
      ret, frame = cap.read()
      if ret:
        output_temp_dir = 'C:/Users/jzhan/OneDrive/Documents/GitHub/LaneATT/datasets/tesla-test/temp-' + vidname + '/'
        if not os.path.exists(output_temp_dir):
          os.makedirs(output_temp_dir)
        # if total_frames % 20 == 0: # every 20 frames get the video
        cv2.imwrite(output_temp_dir + str(total_frames).zfill(7) + '.png', frame[:,:,:])
        count += 1 # i.e. at 30 fps, this advances one second
        # cap.set(cv2.CAP_PROP_POS_FRAMES, 30)
        total_frames += 1
      else:
        cap.release()
        break