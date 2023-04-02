clc
clear
close all;

coef =0.85162353515625;
SAMPLE_PERIOD = 1/8000;
delay_1=0;
delay_2=0;
delay=0;
t=0;
freq1 = 697;
for i = 0:205
    input = sin(2.0*3.141592654*freq1 * SAMPLE_PERIOD * t);
    t = t + 1;
    delay= 2* coef *delay_1 + input - delay_2;
    delay_2 = delay_1;
    delay_1 = delay;
    
end

power = delay_1^2 + delay_2^2 - 2*delay_1*delay_2*coef;
disp(power);