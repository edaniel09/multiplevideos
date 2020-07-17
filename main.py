import cv2
import numpy as np

cap = cv2.VideoCapture("35.mp4")
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)

def main():
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
            # Our operations on the frame come here
            #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frameS = cv2.resize(frame, (320, 240))
            # Display the resulting frame
            cv2.imshow('frame', frameS)
        else:
            print("no video")
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return 0


if __name__ == "__main__":
    main()
