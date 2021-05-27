import cv2 as cv


class ImageUtil:
    @staticmethod
    def read_image(path, scale=1):
        img = cv.imread(path)
        scaled_img = ImageUtil.rescaleFrame(frame=img, scale=scale)
        cv.imshow('CV Image Header', scaled_img)
        cv.waitKey(0)

    @staticmethod
    def rescaleFrame(frame, scale=1):
        height = int(frame.shape[0] * scale)
        width = int(frame.shape[1] * scale)

        dimensions = (width, height)

        return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)