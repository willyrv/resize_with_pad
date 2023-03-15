import cv2
from resize_with_pad_opencv import resize_with_pad
"""
Test the script using multiple dimensions
"""


dimensions_list = [(200, 200), (100, 200), (200, 100), 
                   (900, 900), (1200, 900), (900, 1200),
                   (1200, 200), (200, 1200)]

if __name__ == "__main__":
    PATH2IMAGE = "./kodim01.png"
    NEW_SHAPE = (256, 256)
    PADDING_COLOR = (0, 0, 0)
    image = cv2.imread(PATH2IMAGE)
    for shape in dimensions_list:
        print("Resizing to {}".format(shape))
        resized_image = resize_with_pad(image, shape, PADDING_COLOR)
        cv2.imshow("Padded image", resized_image)
        cv2.waitKey()


