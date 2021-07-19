import cv2
import time
import os
import numpy as np
import datetime
import requests

# 2160p: 3840x2160
# 1440p: 2560x1440
# 1080p: 1920x1080
# 720p: 1280x720
# 480p: 854x480
# 360p: 640x360
# 240p: 426x240
#save = cv2.VideoWriter(datapath, cv2.VideoWriter_fourcc(*'X264'), fps , output_size )
# cv2.VideoWriter_fourcc(*'X264') : chuan anh
# fps: so frame/s de luu vao
#output_size : size frame: quality

# Syntax : cv2.putText(frame, Text, (leftpad, bottompad), font, size, color, thickness)

# Parameters:
# frame: current running frame of the video.
# Text: The text string to be inserted.
# org: left-bottom corner of the text string
# font: the type of font to be used.
# color: the colour of the font.
# thickness: the thickness of the font


class CaptureVideo:
    WIDTH = 640  #default 480p
    HEIGHT = 480
    def __init__(self, fps, resolution, path):  # path la chi dinh video - 0 la webcam laptop
        self.fps = fps
        self.path = path
        self.resolution = resolution
        # if (resolution == 240):
        #     self.WIDTH = 426
        #     self.HEIGHT = 240
        # elif (resolution == 360):
        #     self.WIDTH = 640
        #     self.HEIGHT = 360
        if (resolution == 480):
            self.WIDTH = 640
            self.HEIGHT = 480
        elif (resolution == 720):
            self.WIDTH = 1280
            self.HEIGHT = 720
        elif (resolution == 1080):
            self.WIDTH = 1920
            self.HEIGHT = 1080
        elif (resolution == 1440):
            self.WIDTH = 2560
            self.HEIGHT = 1440
        elif (resolution == 2160):
            self.WIDTH = 3840
            self.HEIGHT = 2160
    
    #datapath la path de luu tru video
    def StreamVideo(self, datapath):
        # FILE_OUTPUT = '/home/lctuan/AI/output.avi'
        if os.path.isfile(datapath):
            os.remove(datapath)
            
        ########################################    
        output_size = (self.WIDTH, self.HEIGHT)
        save = cv2.VideoWriter(datapath, cv2.VideoWriter_fourcc(*'XVID'), 10 , output_size )
        cap = cv2.VideoCapture(self.path)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.WIDTH)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.HEIGHT)
        frame_rate = self.fps
        ########################################
        
        prev = 0
        currentFrame = 0
        locTime = 0
        
        while True:
            ret, frame = cap.read()
            
            font = cv2.FONT_HERSHEY_DUPLEX#cv2.FONT_HERSHEY_SIMPLEX  #font for string
            priod = time.time() - prev
            getloc = time.time() - locTime
            
            #get time date
            dt = datetime.datetime.today()
            strDay = dt.strftime('%Y-%m-%d %H:%M:%S')
            strFile = dt.strftime('%Y%m%d_%H%M%S.png')
             
            #get location
            if getloc >= 1:
                locTime = time.time()
                ip_request = requests.get('https://get.geojs.io/v1/ip.json')
                myip = ip_request.json()['ip']
                geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + myip + '.json'
                geo_request = requests.get(geo_request_url)
                location = geo_request.json()
                strLocation = '%sN %sE' %(location['latitude'], location['longitude'])
            size_frameWidth = self.WIDTH
            size_frameHeight = self.HEIGHT
            size = float(size_frameWidth)/1200
            # print(size)
            if priod >= 1./frame_rate:
                prev = time.time()
                frame = cv2.flip(frame, 1)
                    
                    #writing string in frame
                frames = cv2.putText(frame, 'VN001', (int(size_frameWidth*2/48), int(size_frameHeight*2/48))
                                        , font, size, (255, 255, 255), 1, cv2.LINE_AA)
                frames = cv2.putText(frame, '0KM/H', (int(size_frameWidth*42/48), int(size_frameHeight*2/48))
                                        , font, size, (255,255,255), 1, cv2.LINE_AA)
                frames= cv2.putText(frame,strDay, (int(size_frameWidth*26/48), int(size_frameHeight*2/48))
                                        , font, size, (255, 255, 255), 1, cv2.LINE_AA)
                frames = cv2.putText(frame, strLocation, (int(size_frameWidth*2/48), int(size_frameHeight*46/48))
                                        , font, size, (255,255,255), 1, cv2.LINE_AA)
                save.write(cv2.resize(frames,output_size))
                    # ims = cv2.resize(frame, (self.WIDTH, self.HEIGHT))
                cv2.imshow('frame', frames)  #show frame   
            # time.sleep(1./frame_rate)
                cv2.imwrite('/home/lctuan/AI/VN0001_' + strFile, frames) # save img
            k = cv2.waitKey(1)
            if (k == ord('q')):
                break
        cap.release()
        save.release()
        cv2.destroyAllWindows()
        

    
    