% Author: Murat Kirtay, Robotics Laboratory
% Date: 10/01/2015
% Description: Create IO matrices for CNN
% Notes: none
% Bugs: No Known.
function [mat_x, mat_y] = createIOMatrix(data_path, image, network)

file_list = fullfile(data_path, '*.jpg')
files = dir(file_list);
f_size = size(files, 1);

mat_x = [];
mat_y = [];

for i = 1 : f_size,
   
    file = fullfile(data_path,files(i, 1).name);
    fname = files(i, 1).name;
    ind = regexp(fname, '-*-');
    out_class = str2double(fname(ind(1) + 1 : ind(2) - 1))
   
    binary_img = image_proc_steps( file, image );
    inp_vec = createInputVector(binary_img, image);
    out_vec = createOutputVector(out_class, network.num_of_class)
    
    % mat_x' and mat_y' can be used.
    mat_x = [mat_x ; inp_vec];
    mat_y = [mat_y ; out_vec];
end

end