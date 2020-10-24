clear; clc; close all;
iters = 10000000; %evaling at 10 million x points in the interval 0,1
functevals = zeros(1,iters);
low = 0;
upp = 1;
diff = upp-low;
functionAve = 0;
histobins = 100;
results = zeros(1,histobins);

for j = 1:histobins
for i = 1:length(functevals)
    functevals(i) = evalFunct((low + (upp-low).*rand(1,1))); %a + (b-a).*rand(N,1).
end
functionAve = (1/iters)*sum(functevals);
results(j) = diff*functionAve;
end
histogram(results)
% functionAve = (1/iters)*sum(functevals);
% fprintf('The integral of e^(x^2) on the interval %d, %d is ~ %f',low,upp,functionAve*diff);
