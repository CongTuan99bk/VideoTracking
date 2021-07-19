import video as vd
import datetime

dt = datetime.datetime.today()
strDay = dt.strftime('test_%Y%m%d')
cap = vd.CaptureVideo(60, 480, '/dev/video2')
cap.StreamVideo('/home/lctuan/AI/' + strDay + '.avi')