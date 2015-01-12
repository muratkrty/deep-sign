# Author: Murat Kirtay, Robotics Laboratory
# Date: 12/01/2015
# Description: Data set preparetion for DeepSign project
# Notes: 0- Change shutil.copyfile(f_path, fd_name) to
#           shutil.move(f_path, fd_name)
# Bugs: OK. NO Known

import os
import re 
import shutil

data_dir = './DATASET/'
target_dir = './CLASS_SET/'

def create_sub_folder_list(data_dir, target_dir, f_pos, f_neg):
    """ Traverse along target directory and extract path list. """
    
    path_list = []
    for dir_name, sub_dir_names, file_names in os.walk(data_dir):
        for sub_dir_name in sub_dir_names:        
            path = os.path.join(target_dir, sub_dir_name) 
            print path
            path_list.append(os.path.join(path, f_neg))
            path_list.append(os.path.join(path, f_pos))

    return path_list

def create_sub_folders(folder_list):
    """ Create fraud and real sub folder in target_dir subfolders. """
    for s_folder in folder_list:
        print s_folder
        if not os.path.exists(s_folder):
            os.makedirs(s_folder)

def relocate_files(data_dir, target_dir):
    ''' Move each image from DATASET to relevand target_dir and 
        relocate to fraud and real folders.
    '''
    for dir_name, sub_dir_names, file_names in os.walk(data_dir):
        for file_name in file_names:
            f_path = os.path.join(dir_name, file_name)
            class_dir = target_dir + dir_name[len(data_dir):len(dir_name)]
            df_name = os.path.join(class_dir, 'fraud')
            dr_name = os.path.join(class_dir, 'real')
            if re.match('^cf', file_name):
                fd_name = os.path.join(df_name, file_name)
            else:
                fd_name = os.path.join(dr_name, file_name)
            shutil.copyfile(f_path, fd_name)
            
def main():
    path_list = create_sub_folder_list(data_dir, target_dir, 'real', 'fraud')
    create_sub_folders(path_list)
    relocate_files(data_dir)


if __name__ == '__main__':
    main()

    
