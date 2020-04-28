# Financial Engineering  學習歷程  R08323002

#### 作業四: 含股息的 Black-Scholes 選擇權定價模型

## 先說程式執行方法

這支程式是用Python3寫成的，在支援Python的IDE或終端機直接執行HW4目錄下的hw4_r08323002.py檔案，就可以依程式提示輸入股票價格，流動性，除息資訊，無風險利率，履約價格，到期時間等，程式會直接印出計算結果。注意需載入math模組。


## 甚麼是選擇權
see [參考資料1](https://wiki.mbalib.com/zh-tw/%E6%9C%9F%E6%9D%83)  
>選擇權是一種能在未來某特定時間以特定價格買入或賣出一定數量的某種特定商品的權利。它是在期貨的基礎上產生的一種金融工具，給予買方（或持有者）購買或出售標的資產的權利。選擇權的持有者可以在該項選擇權規定的時間內選擇買或不買、賣或不賣的權利，他可以實施該權利，也可以放棄該權利，而選擇權的出賣者則只負有選擇權合約規定的義務。  

## 甚麼是 Black-Scholes 定價模型
see [參考資料2](https://wiki.mbalib.com/zh-tw/Black-Scholes%E6%9C%9F%E6%9D%83%E5%AE%9A%E4%BB%B7%E6%A8%A1%E5%9E%8B)
>
斯克爾斯(Myron Scholes)與他的同事、已故數學家費雪·布萊克(Fischer Black)在70年代初合作研究出了一個期權定價的複雜公式。與此同時，默頓(Robert Merton)也發現了同樣的公式及許多其它有關期權的有用結論。結果，兩篇論文幾乎同時在不同刊物上發表。所以，布萊克—斯克爾斯定價模型亦可稱為布萊克—斯克爾斯—默頓定價模型。默頓擴展了原模型的內涵，使之同樣運用於許多其它形式的金融交易。他們創立和發展的布萊克——斯克爾斯期權定價模型(Black Scholes Option Pricing Model)為包括股票、債券、貨幣、商品在內的新興衍生金融市場的各種以市價價格變動定價的衍生金融工具的合理定價奠定了基礎。

## 程式流程圖

<img src="/HW4/hw4_flow.png" width = "400" height = "640" border="10" />

## 具體計算流程細節

#### 計算扣掉股息現值的股票價格
如果發放股息是市場上公開的資訊，原本的股票價格須扣所有股息的現值。S^hat = S - sum_i ( 第i次股息的無風險利率現值 )  
#### 以 Black-Scholes 公式計算買權價格
call_price = S^hat * N(d1) - X * exp(-r*tau) * N(d2)  
d1 = ( ln(S^hat/X) + ( r + sigma^2/2 )*tau )/( sigma*sqrt(tau) )  
d2 = d1 - sigma*sqrt(tau)  

其中S^hat為除息後股票現值，X為履約價格，r為無風險年化連續利率，tau為時間(年)，sigma為股票流動性，N(d) 為標準常態分布的累積分布函數。  

#### 以 put-call parity 計算賣權價格
由買賣權平價關係 put_price = call_price - S^hat + X * exp(-r*tau) ，計算賣權價格。  

## 執行範例

### 執行版本
```
wwctw@gentoo ~/fe/ps4 $ python
```
```
Python 3.6.5 (default, Jul 16 2019, 13:36:36) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
```
### 執行結果
註: 需載入math模組

```
wwctw@gentoo ~/fe/ps4 $ python hw4_r08323002.py 
```
```
   請輸入現在股票價格 :  75
   請輸入年度化波動 sigma :  0.35
   請輸入無風險年化連續複利利率(%) :  6
   請輸入履約價格 :  65
   請輸入到期時間(月) :  6
   請輸入除息次數 :  2

   第 1 次除息時間和金額的資訊
     請輸入除息時間(月) :  1
     請輸入除息金額 :  1

   第 2 次除息時間和金額的資訊
     請輸入除息時間(月) :  4
     請輸入除息金額 :  1


   輸出結果 :  

   除息後股票現值為    73.025 
   買權價值為    12.806 
   賣權價值為     2.860 

```

## 心得
> 曾經見過 Robert Merton 本人，讓我對這個模型多了幾分敬意
