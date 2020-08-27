clc; clear all; close all;
%% this section generates the vector of collatz numbers
usernum = input('Analysis up to Which Number? ');
numarr = CollatzNum.empty(0,usernum);
for i = 1:usernum
    numarr(i) = CollatzNum(i);
end
%% this section of code plots the result of applying collatz to all numbers in the numarr array
%filling the number array
nums = zeros(1,usernum);
for j = 1:usernum
    nums(j) = numarr(j).num;
end
%filing the collatz length array
collatznum = zeros(1,usernum);
for k = 1:usernum
    collatznum(k) = numarr(k).collatz_count;
end
plot(nums,collatznum)
titlelstr = sprintf('Collatz Graph for numbers %d to %d',nums(1),nums(length(nums)));
title(titlelstr);
xlabel('Numbers')
ylabel('Collatz Length')
%% this section of code prints the 10 numbers which had the largest collatz path length
[~, ind] = sort([numarr.collatz_count],'descend');
sortednumarr = numarr(ind);
for l = 1:10
    fprintf('The number of %d had a collatz length of %d ', sortednumarr(l).num,sortednumarr(l).collatz_count);
    fprintf('\n')
end