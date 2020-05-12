# Financial Engineering  學習歷程  R08323002

#### 作業五: 基於Hull-White利率模型的選擇權定價模型

## 先說程式執行方法

這支程式是用Python3寫成的，在支援Python的IDE或終端機直接執行HW5目錄下的hw5_r08323002.py檔案，就可以依程式提示輸入模型參數，股票價格，選擇權資訊等，程式會直接印出計算結果。注意需載入numpy，QuantLib，matplotlib.pyplot。


## 甚麼是選擇權
see [參考資料1](https://wiki.mbalib.com/zh-tw/%E6%9C%9F%E6%9D%83)  
>選擇權是一種能在未來某特定時間以特定價格買入或賣出一定數量的某種特定商品的權利。它是在期貨的基礎上產生的一種金融工具，給予買方（或持有者）購買或出售標的資產的權利。選擇權的持有者可以在該項選擇權規定的時間內選擇買或不買、賣或不賣的權利，他可以實施該權利，也可以放棄該權利，而選擇權的出賣者則只負有選擇權合約規定的義務。  

## 甚麼是 Hull-White 利率模型
see [參考資料2](https://en.wikipedia.org/wiki/Hull%E2%80%93White_model)
>In financial mathematics, the Hull–White model is a model of future interest rates. In its most generic formulation, it belongs to the class of no-arbitrage models that are able to fit today's term structure of interest rates. It is relatively straightforward to translate the mathematical description of the evolution of future interest rates onto a tree or lattice and so interest rate derivatives such as bermudan swaptions can be valued in the model. The first Hull–White model was described by John C. Hull and Alan White in 1990. The model is still popular in the market today.

## 甚麼是幾何布朗運動
see [參考資料3](https://en.wikipedia.org/wiki/Geometric_Brownian_motion)
>A geometric Brownian motion (GBM) (also known as exponential Brownian motion) is a continuous-time stochastic process in which the logarithm of the randomly varying quantity follows a Brownian motion (also called a Wiener process) with drift.[1] It is an important example of stochastic processes satisfying a stochastic differential equation (SDE); in particular, it is used in mathematical finance to model stock prices in the Black–Scholes model.

## 程式流程圖

<img src="/HW5/hw5_flow.png" width = "336" height = "528" border="10" />

## 具體計算流程細節
#### 以 Hull-White 模型產生利率
此模型假設利率符合隨機微分方程 dr = (\theta - a r) dt + \sigma dW ，其中 a 和 sigma 為常數， \theta 為時間t的函數。  
程式依據使用者輸入的次數產生數條路徑，產生方式可參考此網站 ( see [參考資料4](http://gouthamanbalaraman.com/blog/hull-white-simulation-quantlib-python.html) )  
程式中可以選擇排除負利率與否，如果選擇排除，當發生負利率時，程式會重新產生一條新的路徑。

#### 以幾何布朗運動產生未來股票價格
如果發放股息是市場上公開的資訊，原本的股票價格須扣所有股息的現值，S^hat = S - sum_i ( 第i次股息的無風險利率現值 )  
( see [參考資料5](https://ch-hsieh.blogspot.com/2012/04/how-to-solve-sde-practically-4.html) )
( see [參考資料6](https://colab.research.google.com/drive/1LL_m1UO_U2oHDMQhBDPjhUBANDpVhev7) )
#### 以 Black-Scholes 公式計算買權價格
call_price = S^hat * N(d1) - X * exp( -r * tau) * N(d2)  
d1 = ( ln(S^hat/X) + ( r + sigma^2/2 ) * tau )/( sigma * sqrt(tau) )  
d2 = d1 - sigma * sqrt(tau)  

其中S^hat為除息後股票現值，X為履約價格，r為無風險年化連續利率，tau為時間(年)，sigma為股票流動性，N(d) 為標準常態分布的累積分布函數。  

#### 以 put-call parity 計算賣權價格
由買賣權平價關係 put_price = call_price - S^hat + X * exp( -r * tau) ，計算賣權價格。  

## 執行範例

注意程式中可以選擇折現方式和是否允許負利率。

```
   請輸入蒙地卡羅次數 :  1000

   這期間總共要分幾步模擬 :  3000

   請輸入Hull-White Model 的 sigma 值 :  .1

   請輸入 Hull-White Model 的 a 值 :  .1

   允許負利率嗎  1 允許  2 不允許 :  1

   請輸入現在的年化利率(%) :  3

   請輸入現在股票價格 :  120

   請輸入到期時間(年) :  .75

   請輸入履約價格 :  130

   請輸入股票年度化波動 sigma :  .1

   1 使用模擬出的利率折現  2 輸入無風險利率折現 :  2

   請輸入年化無風險利率(%) :  3
 
```

<img src="/HW5/hw5_ex01.png" width = "383" height = "264" border="10" />
   
<img src="/HW5/hw5_ex02.png" width = "378" height = "264" border="10" />

```

   買權價格為     1.917 

   賣權價值為     8.671 

```

## 心得
> 這兩周的課程內容有點困難，或許要花些心力來複習。
