% Author: Murat Kirtay, Robotics Laboratory
% Date: 10/01/2015
% Description: Prepare output vector
% Notes: none
% Bugs: No Known.
%
function [ out_vec ] = createOutputVector( class_number, num_of_class )

    out_vec = zeros(1, num_of_class);
    out_vec(1, class_number) = 1;

end

