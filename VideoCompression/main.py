'''
Program: Records a video and provides an original version and a compressed version
Teacher: Nandhini Namasivayam
Student Author: Raul Martinez Luna
Started: April 22nd, 2022
Finished: May 10th, 2022
'''

''' Libraries'''
import time
from video import Video

if __name__ == '__main__':
    start_time = time.time()
    program = Video('Video/video.mp4', 'Video/videoUncompressed.avi', 'Video/videoCompressed.avi', 24.0, 1280, 720)
    program.create()
    print("Time taken to execute program: "+str(time.time()-start_time)+" seconds")