function [count] = calc_collatz_length(num)
%this function counts how long it takes for the input num to boil down to 1
count = 0;
if(num==1) %base case check for if the passed number is 1.
    return
end

while(num>1)
    if mod(num,2)==0
        num = num/2;
        count = count+1;
    else
        num = 3*num+1;
        count = count+1;
    end
    
    if count>=1000 %checks for a number that has diverged
        fprintf('%d diverges! ',num)
        return
    end 
end
end