import cv2 as cv


class ImageUtil:
    @staticmethod
    def read_image(path):
        img = cv.imread(path)
        cv.imshow('CV Image Header', img)
        cv.waitKey(0)

