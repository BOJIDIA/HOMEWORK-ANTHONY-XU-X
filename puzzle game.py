  import cv2 as cv
  import random
  from typing import *
  
  def split_image_into_half_randomly(image: List [List[List[List]]]) -> Tuple[List[List[List[int]]]]:
      """
      The function will take a 3D List of an image and split the image in half
      The portion of the split is choosen randomly
      It returns the split images
      """
      nrow = image.shape[0] 
      ncol = image.shape[1]  
      random_row = random.randint(nrow//3, nrow) 
      random_col = random.randint(ncol//3, ncol) 
      
      img1 = image[:random_row, : random_col]
      img2 = image[:random_row, : random_col:]
      img3 = image[:random_row, : random_col]
      img4 = image[:random_row, : random_col:]
      
      return img1, img2, img3, img4
      
if __ name__ == "__main__":
    image = cv.imread("asset/sunglass_cat.jpeg")
    image_partitions = split_image_into_four_randomly(image)
    i = 1
    for image in image_partitions:
      image_partitions_partitions = split_image_into_four_randomly(images)
      for fragment_images in image _partitions_partitions:
        cv.imwrite(f"image_{i}.jpg", fragment_images)
        i += 1
        