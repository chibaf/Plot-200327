# HNGN74-200327 plot

""" HNGN001 Created on Tue Jun 11 08:34:11 2019
(two days before 190613) (1month before 190711)"""

import matplotlib.pyplot as plt
import numpy as np

def S(FAI, b):  # function definition
	C=1
	Nu=1
	r=C*(1-FAI)/(FAI**3+b)
	return r
	
# b=0.1, 1, 10, 100

phi = np.arange(0, 1.0, 0.1)  # 0 <= phi <= 0.9, step=0.1 x軸

b=0.1
y1 = S(phi,b)
#plt.plot(phi, y)
#plt.show()

b=1
y2 = S(phi,b)
#plt.plot(phi, y)
#plt.show()

b=10
y3 = S(phi,b)
#plt.plot(phi, y)
#plt.show()

b=100
y4 = S(phi,b)
#plt.plot(phi, y)
#plt.show()

fig, ax = plt.subplots()

c1,c2,c3,c4 = "blue","green","red","black"      # 各プロットの色
l1,l2,l3,l4 = "b=0.1","b=1","b=10","b=100"   # 各ラベル

ax.set_xlabel('phi')  # x軸ラベル
ax.set_ylabel('S')  # y軸ラベル
ax.set_title(r'HNGN74') # グラフタイトル
# ax.set_aspect('equal') # スケールを揃える
#ax.grid()            # 罫線
#ax.set_xlim([-10, 10]) # x方向の描画範囲を指定
#ax.set_ylim([0, 1])    # y方向の描画範囲を指定
ax.plot(phi, y1, color=c1, label=l1)
ax.plot(phi, y2, color=c2, label=l2)
ax.plot(phi, y3, color=c3, label=l3)
ax.plot(phi, y4, color=c4, label=l4)
ax.legend(loc=0)    # 凡例
fig.tight_layout()  # レイアウトの設定
# plt.savefig('hoge.png') # 画像の保存
plt.show()