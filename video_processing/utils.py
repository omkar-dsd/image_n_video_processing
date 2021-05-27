import cv2 as cv


class VideoUtil:
    @staticmethod
    def read_video(path, scale=1):
        capture = cv.VideoCapture(path)
        while True:
            flag, frame = capture.read()
            scaled_frame = VideoUtil.rescaleFrame(frame=frame, scale=scale)
            cv.imshow('CV Video Header', scaled_frame)

            if cv.waitKey(20) & 0xFF == ord('d'):
                break
        
        capture.release()
        cv.destroyAllWindows()

    @staticmethod
    def rescaleFrame(frame, scale=1):
        height = int(frame.shape[0] * scale)
        width = int(frame.shape[1] * scale)

        dimensions = (width, height)

        return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
