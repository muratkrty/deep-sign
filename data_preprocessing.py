# Author: Murat Kirtay, Robotics Laboratory
# Date: 12/01/2015
# Description: Data set preparetion for DeepSign project
# Notes: 0- Change shutil.copyfile(f_path, fd_name) to
#           shutil.move(f_path, fd_name) for JIT processing.
#        1- Remember os.walk walks recursively, so it is better to 
#           create folders in different directories.
#        2- Once you run main,  it will autmatically prepare testing and 
#           training files/folders.
# Bugs: OK. NO Known

import os
import re 
import shutil

data_dir = './DATASET/'
target_dir = './CLASS_SET/'
network_dir = './NETWORK_DATA/'

def create_sub_folder_list(data_dir, target_dir, f_pos, f_neg):
    """ Traverse along target directory and extract path list. """
    path_list = []
    for dir_name, sub_dir_names, file_names in os.walk(data_dir):
        for sub_dir_name in sub_dir_names:        
            path = os.path.join(target_dir, sub_dir_name) 
            path_list.append(os.path.join(path, f_neg))
            path_list.append(os.path.join(path, f_pos))

    return path_list

def create_sub_folders(folder_list):
    """ Create fraud and real sub folder in target_dir subfolders. """
    for s_folder in folder_list:
        if not os.path.exists(s_folder):
            os.makedirs(s_folder)

def relocate_files(data_dir, target_dir):
    """ Move each image from DATASET to relevand target_dir and 
        relocate to fraud and real folders.
    """
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

def create_real_user_data_set(data_dir, net_dir, training_size):
    """ Create training and test folders from real signature owners for 
        convolutional network's input an output.
        user can be either real or fraud
    """
    for dir_name, sub_dir_names, file_names in os.walk(data_dir):
        ind = 1
        for file_name in file_names:
            file_path = os.path.join(dir_name, file_name)
            if re.search(r'real', file_path):
                if ind <= training_size:
                    tr_path = os.path.join(net_dir[0], file_name)
                    if not os.path.exists(tr_path):
                        shutil.copyfile(file_path, tr_path)
                else:
                    tst_path = os.path.join(net_dir[1], file_name)
                    if not os.path.exists(tst_path):
                        shutil.copyfile(file_path, tst_path)
                
                ind = ind + 1

def create_fraud_user_data_set(data_dir, net_dir, training_size):
    """ Create training and test folders from real signature owners for 
        convolutional network's input an output.
        
    """
    for dir_name, sub_dir_names, file_names in os.walk(data_dir):
        ind = 1
        for file_name in file_names:
            file_path = os.path.join(dir_name, file_name)
            if re.search(r'fraud', file_path) and ind <= 24:
                if ind <= training_size:
                    tr_path = os.path.join(net_dir[2], file_name)
                    if not os.path.exists(tr_path):
                        shutil.copyfile(file_path, tr_path)
                else:
                    tst_path = os.path.join(net_dir[3], file_name)
                    if not os.path.exists(tst_path):
                        shutil.copyfile(file_path, tst_path)
                
                ind = ind + 1


def main():
    
    tot_real_sign = 24
    tot_fraud_sign = 32
    training_size = 18

    path_list = create_sub_folder_list(data_dir, target_dir, 'real', 'fraud')
    create_sub_folders(path_list)
    relocate_files(data_dir)
    
    network_dir_list = [network_dir+'training_real/', network_dir+'testing_real', 
                        network_dir+'training_fraud', network_dir+'testing_fraud']
    
    create_sub_folders(network_dir_list)

    create_real_user_data_set(target_dir, network_dir_list, training_size)
    create_fraud_user_data_set(target_dir, network_dir_list, training_size)    
    

if __name__ == '__main__':
    main()

    
