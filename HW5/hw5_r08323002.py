# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import QuantLib as ql

# 輸入參數
S0 = float(input("   請輸入現在股票價格 :  "))
length = float(input("   請輸入到期時間(年) :  "))
strike = float(input("   請輸入履約價格 :  "))
risk_free = float(input("   請輸入年化無風險利率(%) :  "))/100
num_paths = int(input("   請輸入蒙地卡羅次數 :  "))
timestep = int(input("   這期間總共要分幾步模擬 :  "))
sigma = float(input("   請輸入Hull-White Model 中年度化波動 sigma 的值 :  "))
a = float(input("   請輸入 Hull-White Model 中 a 的值 :  "))
forward_rate = float(input("   請輸入現在的年化利率(%) :  "))/100


# 用 Hull-White model 產生利率
# 參考資料 :
# http://gouthamanbalaraman.com/blog/hull-white-simulation-quantlib-python.html

np.random.seed(100)

day_count = ql.Thirty360()
todays_date = ql.Date(11, 5, 2020)

ql.Settings.instance().evaluationDate = todays_date

spot_curve = ql.FlatForward(todays_date, \
              ql.QuoteHandle(ql.SimpleQuote(forward_rate)), day_count)
spot_curve_handle = ql.YieldTermStructureHandle(spot_curve)

hw_process = ql.HullWhiteProcess(spot_curve_handle, a, sigma)
rng = ql.GaussianRandomSequenceGenerator( \
       ql.UniformRandomSequenceGenerator(timestep,ql.UniformRandomGenerator()))
seq = ql.GaussianPathGenerator(hw_process, length, timestep, rng, False)

# 每一條路徑利率產生函數
def generate_paths(num_paths, timestep):
    arr = np.zeros((num_paths, timestep+1))
    for i in range(num_paths):
        sample_path = seq.next()
        path = sample_path.value()
        time = [path.time(j) for j in range(len(path))]
        value = [path[j] for j in range(len(path))]
        arr[i, :] = np.array(value)
    return np.array(time), arr

time, paths = generate_paths(num_paths, timestep)
for i in range(num_paths):
    plt.plot(time, paths[i, :], lw=0.8, alpha=0.6)
plt.title("Hull-White Short Rate Simulation")
plt.show()

# 用幾何布朗運動計算股票未來價值
# 參考資料 :
# https://colab.research.google.com/drive/1LL_m1UO_U2oHDMQhBDPjhUBANDpVhev7

np.random.seed(200)

def genBrownPath (T, mu_path, sigma, S0, dt):
    n = len(mu_path)
    W = [0] + np.random.standard_normal(size = n)
    W = np.cumsum(W)*np.sqrt(dt) # == standard brownian motion
    X = (mu_path - 0.5*sigma**2)*dt
    X = np.cumsum(X) + sigma*W
    S = S0*np.exp(X) # == geometric brownian motion
    plt.plot(np.linspace(0, T, n), S)
    return S

stock_paths = []
call = []
put = []

for i in range(0,num_paths):
    stock_paths.append(genBrownPath(length,paths[i],sigma,S0,length/timestep))
    call.append( max(stock_paths[i][-1]-strike,0) )
    put.append( max(strike-stock_paths[i][-1],0) )

plt.title("Stock price simulation")
plt.show()

call_price = np.mean(call)/np.exp(-risk_free*length)
put_price = np.mean(put)/np.exp(-risk_free*length)

print("\n   買權價格為",'%9.3f'%call_price,"\n",end="")
print("\n   賣權價值為",'%9.3f'%put_price,"\n",end="")

