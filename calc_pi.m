clc; clear all; close all;
%this script approximates pi utilizing a user given number of points
user_point_val = input('Enter a # of points: ');
[x_points,y_points] = gen_points(user_point_val );
pointnum = length(x_points);
sqr_area = 1;
pointnum_in_circ = 0;

for i = 1:pointnum
    %pulling generated x,y points
    x = x_points(i);
    y = y_points(i);
    if(check_if_within_circle(x,y))
        pointnum_in_circ = pointnum_in_circ+1;
    end
end

portion_of_points_in_circ = pointnum_in_circ/pointnum;
circ_area = portion_of_points_in_circ*sqr_area;
pi_approx = circ_area/(0.5^2);

fprintf('Pi is about: %f',pi_approx)