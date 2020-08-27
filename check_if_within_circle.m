function eval = check_if_within_circle(x,y)
%(x-0.5)^2 + (y-.0.5)^2 > 0.5^2 --> outside circle
val = (x-0.5)^2 + (y-0.5)^2;
if(val>0.5^2)
    eval = false;
elseif(val<=0.5^2)
    eval = true;
end

