%该文件可播放wav音频，并通过fft分析频谱，对音频进行解码

clear
clc

[x, Fs] = audioread('./audioFile/answer.wav');    %读取wav文件
fprintf('默认抽样频率为：%d\n', Fs);    %查看默认抽样频率Fs
threshold = 600; %判决门限

sound(x, Fs);   % 播放音频

sig_matrix = reshape(x,[length(x)/8 8]); %将声音信息按照每个symbol进行分割
sig_matrix = sig_matrix';

fre_sig_matrix = zeros(size(sig_matrix)); %记录每个部分的频率信息
pad_flag = zeros(8,8);                      %记录每个频率主要包含的频率
fre_label = [697 770 852 941 1209 1336 1477 1633]; %频率列表
pad = ['1', '2', '3' , 'A' ; ...                %字符矩阵
       '4','5','6','B'; ...
       '7','8','9','C' ; ...
       '*','0','#','D'];

for i = 1:8         %通过傅里叶变换，得到0-Fs的频率信息
    fre_sig_matrix(i,:) = abs(fft(sig_matrix(i,:)));
    for j = 1:8 %通过比较各个频率的幅值，判断是否包含该频率
        if fre_sig_matrix(i,1+ round(fre_label(1,j)/Fs*size(sig_matrix,2))) > threshold
            pad_flag(i,j) = 1;
        end
    end
end

hold on %绘制8个部分的频谱
    for i = 1:8
        subplot(8,1,i)
        plot(linspace(0,Fs,length(x)/8) , fre_sig_matrix(i,:))
        %plot( fre_sig_matrix(i,:))
    end
hold off


str = ''; %对各个部分进行解码
for i = 1:8
    for j = 1:4
        if pad_flag(i,j) == 1
            break
        end
    end
    for k = 1:4
        if pad_flag(i,k+4) == 1
            break;
        end
    end
    str = [str,pad(j,k)];

end
fprintf(['解码后的结果为：',str,'\n'])