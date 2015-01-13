% Author: Murat Kirtay, Robotics Laboratory
% Date: 10/01/2015
% Description: Prepare input vector
% Notes: none
% Bugs: No Known.

function [ inp_vec ] = createInputVector( img_mat, image )

inp_vec = reshape(img_mat, 1, image.numrows * image.numcols);

end

