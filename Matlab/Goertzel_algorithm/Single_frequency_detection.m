clc
clear
close all;

coef_1=0.85162353515625;

AMP = 32768;
SAMPLE_PERIOD = 1/8000;
delay_1=0;
delay_2=0;
delay=0;

power_mat = zeros(1,1000);

t=0;
for freq1=1:1000 
    t=0;
    for i = 0:205
        input = AMP * sin(2.0*3.141592654*freq1* SAMPLE_PERIOD * t) + AMP * sin(2.0*3.141592654* 770 * SAMPLE_PERIOD * t);
        t = t+1;
        delay=2*coef_1*delay_1 + input - delay_2;
        delay_2 = delay_1;
        delay_1 = delay;
    end
    power = delay_1^2 + delay_2^2 - 2*delay_1*delay_2*coef_1;
    power_mat(1,freq1)=power;
end
stem(power_mat)





