import cv2
import numpy as np

from typing import Tuple

def resize_with_pad(image: np.array, 
                    new_shape: Tuple[int, int], 
                    padding_color: Tuple[int, int, int] = (255, 255, 255)) -> np.array:
    """Resizes the input image keeping the aspect ratio by adding padding
    using the indicated padding_color.
    Params:
        image: Image to be resized.
        new_shape: (width, height) of new image.
        padding_color: Tuple in BGR of padding color
    Returns:
        image: Resized image with padding
    """
    current_height, current_width, ignore = image.shape
    new_width, new_height = new_shape[0], new_shape[1]
    ratio_h = new_height / current_height
    ratio_w = new_width / current_width
    ratio = min(ratio_h, ratio_w)
    w, h = int(current_width * ratio), int(current_height * ratio)
    resized_img = cv2.resize(image, (w, h))
    delta_w = np.abs(w - new_width)
    delta_h = np.abs(h - new_height)
    top, bottom = delta_h//2, delta_h-(delta_h//2)
    left, right = delta_w//2, delta_w-(delta_w//2)
    resized_img = cv2.copyMakeBorder(resized_img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=padding_color)
    return resized_img
  
if __name__ == "__main__":
    PATH2IMAGE = "./kodim01.png"
    NEW_SHAPE = (256, 256)
    PADDING_COLOR = (0, 0, 0)
    image = cv2.imread(PATH2IMAGE)
    image = resize_with_pad(image, (256, 256), PADDING_COLOR)
    
    cv2.imshow("Padded image", image)
    cv2.waitKey()