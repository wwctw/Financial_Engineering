# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 02:30:27 2020

@author: user01
"""

def ytm(price,par,rate,t_period,payment):
    upper = 1.0
    C = par*rate/payment
    while 1:
        pay_inter = upper/payment
        PV = C*(1-(1+pay_inter)**(-t_period))/pay_inter \
             + par*(1+pay_inter)**(-t_period)
        if PV > price:
            upper = upper + 1.0
        else:
             break
    lower = upper - 1.0
    mid = (lower+upper)/2
    for k in range(1,60):
        pay_inter = mid/payment
        PV = C*(1-(1+pay_inter)**(-t_period))/pay_inter \
             + par*(1+pay_inter)**(-t_period)
        if PV > price:
            lower = mid
        else:
            upper = mid
        mid = (lower+upper)/2
    return (lower+upper)/2

payment = int(input(\
"   請輸入每年計息次數   年計息請輸入 1   半年計息請輸入 2   季計息請輸入 4 :  "))
end_year = float(input("   請輸入總年數 :  "))
total_period = int(end_year*payment)
print('\n   總共有 ',total_period,' 期')

coupon_rate = [0]
bond_price = [1000]

ytm_bond = [0]
spot_rate = [0]
forward_rate = [[]]



for k in range(1,total_period+1):
    print("\n   面額1000元到期時間",'%.2f'%(k/payment),"年債券的債券")
    coupon_rate.append(float(input("     請輸入票面利率(%) :  "))/100)
    bond_price.append(float(input("     請輸入債券價格 :  ")))
    
for k in range(1,total_period+1):
    ytm_bond.append( ytm(bond_price[k],1000,coupon_rate[k],k,payment) )
    temp_price = bond_price[k]
    C = 1000*coupon_rate[k]/payment
    for i in range(1,k):
        temp_price = temp_price - C*(1+spot_rate[i]/payment)**(-i)
    spot_rate.append( (((1000+C)/temp_price)**(1/k)-1)*payment )
    forward_rate.append([spot_rate[k]])
    for i in range(1,k):
        forward_rate[k].append(   ( ( ((1+spot_rate[k]/payment)**k) \
                               /((1+forward_rate[i][0]/payment)**i) \
                                )**(1/(k-i))-1 )*payment   )

print("\n\n   計算結果")
print("\n   到期時間  ",end="")
print("             ",end="")
for k in range(1,total_period+1):
    print(" ",'%8.2f'%(k/payment),"y ",end="")
print("\n   債券價格  ",end="")
print("             ",end="")
for k in range(1,total_period+1):
    print(" ",'%8.2f'%(bond_price[k]),"  ",end="")
print("\n   票面利率  ",end="")
print("             ",end="")
for k in range(1,total_period+1):
    print(" ",'%8.2f'%(coupon_rate[k]*100),"% ",end="")
print("\n   債券殖利率",end="")
print("             ",end="")
for k in range(1,total_period+1):
    print(" ",'%8.2f'%(ytm_bond[k]*100),"% ",end="")
print("\n   即期利率  ",end="")
print("             ",end="")
for k in range(1,total_period+1):
    print(" ",'%8.2f'%(spot_rate[k]*100),"% ",end="")
    
print("\n\n")
print("   遠期利率表",end="")
for k in range(0,total_period+1):
    print(" ",'%8.2f'%(k/payment),"y ",end="")
for k in range(0,total_period+1):
    print("\n",'%8.2f'%(k/payment),"y  ",end="")
    for m in range(0,k+1):
        print("             ",end="")
    for m in range(k+1,total_period+1):
        print(" ",'%8.2f'%(forward_rate[m][k]*100),"% ",end="")
print("\n")
