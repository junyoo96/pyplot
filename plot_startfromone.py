import numpy as np
import matplotlib.pyplot as plt 

x=[i for i in range(1,31)]
print(x)

a = np.array([0.9983,
0.9119,
0.8640,
0.8358,
0.8221,
0.8020,
0.7938,
0.7913,
0.7803,
0.7784,
0.7735,
0.7710,
0.7684,
0.7616,
0.7587,
0.7542,
0.7539,
0.7537,
0.7488,
0.7428,
0.7390,
0.7400,
0.7388,
0.7342,
0.7365,
0.7358,
0.7343,
0.7329,
0.7345,
0.7378])
b = np.array([0.9449,
0.8121,
0.7282,
0.6714,
0.6340,
0.6067,
0.5887,
0.5749,
0.5620,
0.5547,
0.5478,
0.5454,
0.5428,
0.5360,
0.5327,
0.5329,
0.5256,
0.5288,
0.5263,
0.5230,
0.5190,
0.5195,
0.5180,
0.5168,
0.5147,
0.5130,
0.5111,
0.5135,
0.5131,
0.5106])

tmp=[]
for i in range(len(a)+1):
    if i%5==0 or i==1 or i==30:
        if i==0:
            tmp.append('')
        else:
            tmp.append(i)
    else:
        tmp.append('')

plt.figure(figsize=(10,5))
# dim=np.arange(1,31,4)
# plt.xticks(np.arange(len(a),step=1),np.arange(1,len(a)+1),fontsize=16)
plt.xticks(np.arange(len(a)+1),tmp,fontsize=16)
plt.xticks(fontsize=16)
# plt.tick_params(axis='x', which='major', labelsize='large')
plt.yticks(fontsize=16)
plt.xlabel("Epochs",fontsize=20)
plt.ylabel("Feature Distance",fontsize=20)
plt.plot(x,a,'r',label='Baseline',linestyle='dashed',linewidth='3.0')
plt.plot(x,b,'b',label='SelfReg',linewidth='3.0')
plt.legend(loc='upper right',fontsize=15)
plt.xlim(0,31)
plt.show()
