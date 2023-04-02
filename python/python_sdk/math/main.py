# from MathUtils import FundamentalMath, SumUtils

# print(FundamentalMath.fibonacci(30))

# nums = [-1,0,1,2,-1,-4]
# print(SumUtils.threeSum(nums))

import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.arange(0.05, 20, 0.05, dtype = np.double)
print(x)
xdb = []
for i in range(len(x)):
    mid_xdb = 10 * math.log10(x[i])
    xdb.append(mid_xdb)

y = []
for i in range(len(x)):
    mid_y = 1/2 * math.log((1+x[i]), 2)
    y.append(mid_y)

y1 = []
for i in range(len(x)):
    mid = (math.pi * math.e)/6
    mid_y1 = y[i] - 1/2 * math.log(mid, 2)
    y1.append(mid_y1)

y2 = []
for i in range(len(x)):
    mid = 1 + math.pow(math.pow(2, y[i])/2,2)
    mid_y2 = y1[i] - 1/2* math.log(mid,2)
    y2.append(mid_y2)

y20 = []
for i in range(len(x)):
    mid = math.pow(1/(2 * math.pow(2, -y[i])),2)
    mid_y20 = y1[i] - 1/2* math.log(math.e,2) * mid
    y20.append(mid_y20)


y4 = []
for i in range(len(x)):
    mid = 1 + math.pow(math.pow(2, y[i])/4,2)
    mid_y4 = y1[i] - 1/2 * math.log(mid,2)
    y4.append(mid_y4)

y40 = []
for i in range(len(x)):
    mid = math.pow(1/(2 * math.pow(2, -y[i])),2)
    mid_y40 = y1[i] - 1/4 * math.log(math.e,2) * mid
    y40.append(mid_y40)



y8 = []
for i in range(len(x)):
    mid = 1 + math.pow(math.pow(2, y[i])/8,2)
    mid_y8 = y1[i] - 1/2 * math.log(mid,2)
    y8.append(mid_y8)


y80 = []
for i in range(len(x)):
    mid = math.pow(1/(2 * math.pow(2, -y[i])),2)
    mid_y80 = y1[i] - 1/8 * math.log(math.e,2) * mid
    y80.append(mid_y80)

# y1=y-0.5*log2(pi*exp(1)./6);
# y2=y1-0.5*log2(1+((2.^y)/2).^2);
# y20=y1-(log2(exp(1))./2)*(1./(2*2.^(-1*y))).^2;
# y4=y1-0.5*log2(1+((2.^y)/4).^2);
# y40=y1-(log2(exp(1))./2)*(1./(4*2.^(-1*y))).^2;
# y8=y1-0.5*log2(1+((2.^y)./8).^2);
# y80=y1-(log2(exp(1))./2)*(1./(8*2.^(-1*y))).^2;
 

sub_axix = filter(lambda x:x%200 == 0, xdb)
plt.title('Result Analysis')
plt.plot(xdb, y, color='green', label='x-y')
plt.plot(xdb, y1, color='red', label='x-y1')
plt.plot(xdb, y2, color='black', label='x-y2')
plt.plot(xdb, y20, color='blue', label='x-y20')
plt.plot(xdb, y4, color='black', label='x-y4')
plt.plot(xdb, y40, color='blue', label='x-y40')
plt.plot(xdb, y8, color='black', label='x-y8')
plt.plot(xdb, y80, color='blue', label='x-y80')
plt.legend()

plt.xlabel('xdb')
plt.ylabel('result')
plt.show()
