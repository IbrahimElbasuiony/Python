import cv2
import os


outputdir = "Frames"

if not os.path.exists(outputdir):
    os.mkdir(outputdir)


video_path = r"C:\Users\ibrah\Downloads\Video\3 Hours of Amazing Nature Scenery & Relaxing Music for Stress Relief..mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

frame_count = 0


while True:

    rat,frame = cap.read()


    if not rat :
        break

    frame_filename = os.path.join(outputdir, f'frame_{frame_count:04d}.jpg')
    cv2.imwrite(frame_filename, frame)

    frame_count += 1

cap.release()
cv2.destroyAllWindows()


