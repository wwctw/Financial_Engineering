# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import QuantLib as ql

# 輸入參數

num_paths = int(input("   請輸入蒙地卡羅次數 :  "))
timestep = int(input("   這期間總共要分幾步模擬 :  "))
sigma = float(input("   請輸入Hull-White Model 的 sigma 值 :  "))
a = float(input("   請輸入 Hull-White Model 的 a 值 :  "))
negative = int(input("   允許負利率嗎  1 允許  2 不允許 :  "))
forward_rate = float(input("   請輸入現在的年化利率(%) :  "))/100
S0 = float(input("   請輸入現在股票價格 :  "))
length = float(input("   請輸入到期時間(年) :  "))
strike = float(input("   請輸入履約價格 :  "))
sigma_stock = float(input("   請輸入股票年度化波動 sigma :  "))
pv_method = int(input("   1 使用模擬出的利率折現  2 輸入無風險利率折現 :  "))
if pv_method == 2:
    risk_free = float(input("   請輸入年化無風險利率(%) :  "))/100

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
        while 1:
            sample_path = seq.next()
            path = sample_path.value()
            time = [path.time(j) for j in range(len(path))]
            value = [path[j] for j in range(len(path))]
            # 若允許負利率，則不須判斷是否發生負利率
            if negative == 1:
                break
            # 若不允許負利率，發生負利率時須重新產生路徑
            for k in range(0,len(value)):
                if value[k]<0:
                    break
            if k == (len(value)-1):
                break
        arr[i, :] = np.array(value)
    return np.array(time), arr

time, paths = generate_paths(num_paths, timestep)
# 將利率路徑畫出來
for i in range(num_paths):
    plt.plot(time, paths[i, :], lw=0.8, alpha=0.6)
plt.title("Hull-White Short Rate Simulation")
plt.show()

# 用幾何布朗運動計算股票未來價值
# 參考資料 :
# https://colab.research.google.com/drive/1LL_m1UO_U2oHDMQhBDPjhUBANDpVhev7

np.random.seed(200)

def genBrownPath (T, mu_path, sigma_stock, S0, dt):
    n = len(mu_path)
    W = [0] + np.random.standard_normal(size = n)
    W = np.cumsum(W)*np.sqrt(dt) # 產生標準布朗運動
    X = (mu_path - 0.5*sigma_stock**2)*dt # 注意到 mu 會隨時間改變
    X = np.cumsum(X) + sigma_stock*W
    S = S0*np.exp(X) # 產生股票價格
    plt.plot(np.linspace(0, T, n), S) # 將股價畫出來
    return S

stock_paths = []
call = []
put = []

for i in range(0,num_paths):
    stock_paths.append(genBrownPath(length, paths[i], \
                                    sigma_stock, S0, length/timestep ) )
    # 根據不同的折現方式折現
    if pv_method == 2:
        dfactor = np.exp(risk_free*length) # 根據輸入的無風險利率折現
    else:
        dfactor = 0
        for j in range(0,len(paths[i])):
            dfactor = dfactor + paths[i][j]
        dfactor = np.exp(dfactor*length/timestep) # 根據路徑產生的利率折現
    call.append( max(stock_paths[i][-1]-strike,0) / dfactor )
    put.append( max(strike-stock_paths[i][-1],0) / dfactor )

plt.title("Stock price simulation")
plt.show()

# 由期望現值得出選擇權的價格
call_price = np.mean(call)
put_price = np.mean(put)

print("\n   買權價格為",'%9.3f'%call_price,"\n",end="")
print("\n   賣權價值為",'%9.3f'%put_price,"\n",end="")

