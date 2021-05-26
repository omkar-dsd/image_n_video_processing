import cv2 as cv


class VideoUtil:
    @staticmethod
    def read_video(path):
        capture = cv.VideoCapture(path)
        while True:
            flag, frame = capture.read()
            cv.imshow('CV Video Header', frame)

            if cv.waitKey(20) & 0xFF == ord('d'):
                break
        
        capture.release()
        cv.destroyAllWindows()
