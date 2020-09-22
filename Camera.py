import socket

def video():
    import cv2
    vid = cv2.VideoCapture(0) 
  
    while(True): 
      
    # Capture the video frame 
    # by frame 
        ret, frame = vid.read() 
  
    # Display the resulting frame 
        cv2.imshow('Camera', frame) 
      
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
  
# After the loop release the cap object 
    vid.release() 
# Destroy all the windows 
    cv2.destroyAllWindows()

c = socket.socket()

c.bind(('localhost',9498))

c.listen(5)

while True:
    c.send(bytes(video()))

    c.close()

