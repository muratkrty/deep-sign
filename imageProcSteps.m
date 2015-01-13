% Author: Murat Kirtay, Robotics Laboratory
% Date: 10/01/2015
% Description: resize and binarize image
% Notes: none
% Bugs: No Known.

function [ proced_img ] = imageProcSteps( img_name, image )

    img = imread(img_name);
    resized_img = imresize(img, [image.numrows image.numcols])
    bin_img = im2bw(resized_img, image.level);

    proced_img = bin_img

end

