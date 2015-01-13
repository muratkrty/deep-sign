# Author: Murat Kirtay, Robotics Laboratory
# Date: 13/01/2015
# Description: Image set preparation for DeepSign project
# Notes: none.
# Bugs: OK. NO Known

import cv2
import os
import re 
import numpy as np

def img_proc_steps(img):
    """Apply preprocessing steps to convert image as scaled binary image. """
    gray_img = cv2.imread(img, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    binarized_img = cv2.threshold(gray_img, 200, 255, cv2.THRESH_BINARY)[1]
    resized_img = cv2.resize(binarized_img, (256, 128))
    return resized_img

def binarize_and_relocate_image(data_dir):
    ''' Binarize each image in DATASET folder and relocate to 
        fraud and real folders.
    '''
    for dir_name, sub_dir_names, file_names in os.walk(data_dir):
        for file_name in file_names:
            f_path = os.path.join(dir_name, file_name)
            img = img_proc_steps(f_path)
            df_name = os.path.join(dir_name, 'fraud')
            dr_name = os.path.join(dir_name, 'real')
            if re.match('^cf', file_name):
                ff_name = os.path.join(df_name, file_name)
                cv2.imwrite(ff_name, img);
            else:
                rf_name = os.path.join(dr_name, file_name)
                cv2.imwrite(rf_name, img)


def display_image_info(img):
    ''' Display image related various information. '''
    img = cv2.imread(img,0)
    rows,cols = img.shape
    print 'Num of cols: ', cols
    print 'Num of rows: ', rows
    print 'Shape: ', img.shape
    print 'Data type: ',  img.dtype
    print 'Image Matrix:'
    print img 

def matrix_to_array(mat):
    return np.squeeze(np.asarray(mat))


def main():
    #binarize_and_relocate_image(data_dir)
    #traverse_dir(data_dir)
    #path_list = create_sub_folder_list(data_dir, 'real', 'fraud')
    #create_sub_folders(path_list)
    img = 'c-001-01.jpg'
    img2 = cv2.imread(img)
    img_vec = matrix_to_array(img2)
    
    # display_image_info(img)
    # bin_resized_img = img_proc_steps(img)
    # cv2.imshow('Resized and binarized image', bin_resized_img)
    # cv2.waitKey(0)
  
if __name__ == '__main__':
    main()











