# -*- coding: utf-8 -*-

import math

# 輸入股票與選擇權資訊
stock_price = float(input("   請輸入現在股票價格 :  "))
sigma = float(input("   請輸入年度化波動 sigma :  "))
T_div = int(input("   請輸入除息次數 :  "))
r = float(input("   請輸入無風險年化連續複利利率(%) :  "))/100
X = float(input("   請輸入履約價格 :  "))
tau = float(input("   請輸入到期時間(月) :  "))/12
div_time = [0];
div_price = [0];
for k in range(1,T_div+1):
    print("\n   第",'%d'%k,"次除息時間和金額的資訊\n",end="")
    div_time.append(float(input("     請輸入除息時間(月) :  "))/12)
    div_price.append(float(input("     請輸入除息金額 :  ")))

# 計算除息後的現值
exdiv_stock = stock_price
for k in range(1,T_div+1):
    exdiv_stock = exdiv_stock - div_price[k]*math.exp(-r*div_time[k])

# 以 Black-Scholes 公式計算買權價格
d1 = ( math.log(exdiv_stock/X) + (r+sigma*sigma/2)*tau )/sigma/tau**0.5
d2 = d1 - sigma*tau**0.5
cdf1 = ( 1.0 + math.erf(d1/2.0**0.5) )/2.0 # 常態分布累積機率
cdf2 = ( 1.0 + math.erf(d2/2.0**0.5) )/2.0 # 常態分布累積機率
call_price = exdiv_stock*cdf1 - X*math.exp(-r*tau)*cdf2

# 以 put-call parity 計算賣權價格
put_price = call_price - exdiv_stock + X*math.exp(-r*tau)

# 輸出結果
print("\n\n   輸出結果 :  \n\n",end="")
print("   除息後股票現值為",'%9.3f'%exdiv_stock,"\n",end="")
print("   買權價值為",'%9.3f'%call_price,"\n",end="")
print("   賣權價值為",'%9.3f'%put_price,"\n\n",end="")
