# -*- coding: utf-8 -*-

# 債券殖利率計算函數ytm
#   參數:  price: 現在價格  par: 票面價格  rate: 票面利率
#          t_period: 總期數  payment: 每年計息次數
def ytm(price,par,rate,t_period,payment):
    upper = 1.0
    C = par*rate/payment
    # 每次增加100%去找殖利率的整數初始上界
    while 1:
        pay_inter = upper/payment
        PV = C*(1-(1+pay_inter)**(-t_period))/pay_inter \
             + par*(1+pay_inter)**(-t_period)
        if PV > price:     # 該利率得出的現值比價格高代表殖利率比該利率高
            upper = upper + 1.0
        else:              # 該利率得出的現值比價格低代表殖利率比該利率低
             break
    # 利用二分法來找殖利率
    lower = upper - 1.0    # 初始下界
    mid = (lower+upper)/2
    for k in range(1,60):
        pay_inter = mid/payment
        PV = C*(1-(1+pay_inter)**(-t_period))/pay_inter \
             + par*(1+pay_inter)**(-t_period)
        if PV > price:     # 該利率得出的現值比價格高代表殖利率比該利率高
            lower = mid
        else:              # 該利率得出的現值比價格低代表殖利率比該利率低
            upper = mid
        mid = (lower+upper)/2
    return (lower+upper)/2

# 輸入每年計息次數與年數
payment = int(input(\
"   請輸入每年計息次數   年計息請輸入 1   半年計息請輸入 2   季計息請輸入 4 :  "))
end_year = float(input("   請輸入總年數 :  "))
total_period = int(end_year*payment)
print('\n   總共有 ',total_period,' 期')

coupon_rate = [0]    # 票面利率 List
bond_price = [1000]  # 債券價格 List

ytm_bond = [0]       # 債券殖利率 List
spot_rate = [0]      # 即期利率 List
forward_rate = [[]]  # 遠期利率 二維List

# 輸入債券票面利率與價格
for k in range(1,total_period+1):
    print("\n   面額1000元到期時間",'%.2f'%(k/payment),"年債券的債券")
    coupon_rate.append(float(input("     請輸入票面利率(%) :  "))/100)
    bond_price.append(float(input("     請輸入債券價格 :  ")))

# 計算即期利率與遠期利率
for k in range(1,total_period+1):
    ytm_bond.append( ytm(bond_price[k],1000,coupon_rate[k],k,payment) )
    temp_price = bond_price[k]
    C = 1000*coupon_rate[k]/payment # 每一期的利息現金流
    # 計算債券最後一期現金流的現值
    for i in range(1,k):
        temp_price = temp_price - C*(1+spot_rate[i]/payment)**(-i)
    # 計算即期利率
    spot_rate.append( (((1000+C)/temp_price)**(1/k)-1)*payment )
    # 從第0期到第k期的遠期利率和即期利率相同
    forward_rate.append([spot_rate[k]])
    # 計算遠期利率
    for i in range(1,k):
        forward_rate[k].append(   ( ( ((1+spot_rate[k]/payment)**k) \
                               /((1+forward_rate[i][0]/payment)**i) \
                                )**(1/(k-i))-1 )*payment   )

# 輸出結果
#   如果輸出文字超過欄位，可以將輸出訊息複製到文字編輯軟體上，以利觀察輸出結果
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

