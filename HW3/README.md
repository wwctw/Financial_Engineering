# Financial Engineering  學習歷程  R08323002

#### 作業三: 實作二項選擇權定價模型

## 先說程式執行方法

這支程式是用Python3寫成的，在支援Python的IDE或終端機直接執行HW3目錄下的hw3_r08323002.py檔案，就可以依程式提示輸入買權或賣權，履約價格，總期數，利率，股票價格，股票每期變動等，程式會直接印出計算結果。注意需載入math模組。


## 甚麼是選擇權
see [參考資料1](https://wiki.mbalib.com/zh-tw/%E6%9C%9F%E6%9D%83)  
>選擇權是一種能在未來某特定時間以特定價格買入或賣出一定數量的某種特定商品的權利。它是在期貨的基礎上產生的一種金融工具，給予買方（或持有者）購買或出售標的資產的權利。選擇權的持有者可以在該項選擇權規定的時間內選擇買或不買、賣或不賣的權利，他可以實施該權利，也可以放棄該權利，而選擇權的出賣者則只負有選擇權合約規定的義務。  

## 程式流程圖

<img src="/HW3/hw3_flow.png" width = "480" height = "600" border="10" />

## 具體計算流程細節

#### 轉乘期總收益
原本輸入連續複利的利率 r ，需轉成過了一期後的總收益 R ，其中 R = exp(r)。  
#### 未來可能的股票價格
每一期股票會有兩種情況，從 S 變成 S * u 或從 S 變成 S * d ，因為先乘 u 或先乘 d 的順序並不影響結果，所以只需要考慮乘 u 和乘 d 分別乘幾次即可。在第 m 期，乘 d 的次數從 0 到 m 次，共 (m+1) 種可能。  
#### 偽機率
透過買 h 股價值 S 元的股票和 B 元債券建構和選擇權相同收益的投資組合 ，在無套利機會假設下，過了一期之後此組合價值應該要分別和選擇權到下一期的價格相同，即 hSu + RB = O_u ， hSd + RB = O_d ，可得 h = ( O_u - O_d )/( Su - Sd ) ， B = ( uO_d - dO_u )/(( u - d )R) ， 其中 O_u 和 O_d 為選擇權下一期可能的價格。將h和B代回原本的投資組合， hS + B = ( pO_u + (1-p)O_d )/R ，其中 p = ( R - d )/( u - d ) ， 我們稱 p 為偽機率。  
#### 未來可能的股票價格的機率
因為 p 為乘 u 的機率，故 ( 第 m 期有 k 次乘 d 的機率 ) =  p * ( 第 (m-1)期有 k 次乘 d 的機率 ) + (1-p) * ( 第 (m-1) 期有 (k-1) 次乘 d 的機率 ) 。  
#### 選擇權價格
利用逆向歸納法來得到選擇權價格。買權到期的價格為 max( S - X , 0 ) ，賣權到期價格為 max( X - S , 0 ) ，其中 S 為到期時股票價格， X 為履約價格。因為歐式選擇權不能提前履約，且我們不考慮除息等狀況，故每一期的選擇權價格可以由下一期的期望價格折回現值( 除以 R )得到，第 0 期的價格即為題目所求。  
#### 避險比率
避險比率在使用逆向歸納法求得選擇權的價格時一起計算，由前面的 h = ( O_u - O_d )/( Su - Sd ) 得出，其中 O_u 和 O_d 為選擇權下一期可能的價格。  

## 執行範例

### 執行版本
```
wwctw@gentoo ~/fe/ps3 $ python
```
```
Python 3.6.5 (default, Jul 16 2019, 13:36:36) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
```
### 執行結果
註1: 如果輸出文字超過欄位，可以將輸出訊息複製到文字編輯軟體上，以利觀察輸出結果  
註2: 需載入math模組

#### 買權
```
wwctw@gentoo ~/fe/ps3 $ python hw3_r08323002.py 
```
```
   請輸入計算買權價格或賣權價格  買權請輸入 1  賣權請輸入 2 :  1
   請輸入履約價格 :  150
   請輸入總期數 :  3
   請輸入每期連續複利利率(%) :  18.232
   請輸入現在股票價格 :  160
   請輸入次期股票高價與本期價格的比值 :  1.5
   請輸入次期股票低價與本期價格的比值 :  0.5



   輸出結果

   總期數   3 期  R = 1.200  ( 每期連續複利利率 18.232 % ) 
   現在股票價格 160.000  u = 1.500  d = 0.500
   履約價格 150.000 的買權價格為 85.069

   股票價格表 ( 括弧內為機率 )
         n =  000      n =  001      n =  002      n =  003
          160.000       240.000       360.000       540.000
         ( 1.000 )     ( 0.700 )     ( 0.490 )     ( 0.343 )
                         80.000       120.000       180.000
                       ( 0.300 )     ( 0.420 )     ( 0.441 )
                                       40.000        60.000
                                     ( 0.090 )     ( 0.189 )
                                                     20.000
                                                   ( 0.027 )

   選擇權價值表 ( 括弧內為避險比率 )
         n =  000      n =  001      n =  002      n =  003
           85.069       141.458       235.000       390.000
       (   0.820 )   (   0.906 )   (   1.000 )
                         10.208        17.500        30.000
                     (   0.219 )   (   0.250 )
                                        0.000         0.000
                                   (   0.000 )
                                                      0.000
                                              
```
#### 賣權
```
wwctw@gentoo ~/fe/ps3 $ python hw3_r08323002.py 
```
```
   請輸入計算買權價格或賣權價格  買權請輸入 1  賣權請輸入 2 :  2
   請輸入履約價格 :  150
   請輸入總期數 :  3
   請輸入每期連續複利利率(%) :  18.232
   請輸入現在股票價格 :  160
   請輸入次期股票高價與本期價格的比值 :  1.5
   請輸入次期股票低價與本期價格的比值 :  0.5



   輸出結果

   總期數   3 期  R = 1.200  ( 每期連續複利利率 18.232 % ) 
   現在股票價格 160.000  u = 1.500  d = 0.500
   履約價格 150.000 的賣權價格為 11.875

   股票價格表 ( 括弧內為機率 )
         n =  000      n =  001      n =  002      n =  003
          160.000       240.000       360.000       540.000
         ( 1.000 )     ( 0.700 )     ( 0.490 )     ( 0.343 )
                         80.000       120.000       180.000
                       ( 0.300 )     ( 0.420 )     ( 0.441 )
                                       40.000        60.000
                                     ( 0.090 )     ( 0.189 )
                                                     20.000
                                                   ( 0.027 )

   選擇權價值表 ( 括弧內為避險比率 )
         n =  000      n =  001      n =  002      n =  003
           11.875         5.625         0.000         0.000
       (  -0.180 )   (  -0.094 )   (   0.000 )
                         34.375        22.500         0.000
                     (  -0.781 )   (  -0.750 )
                                       85.000        90.000
                                   (  -1.000 )
                                                    130.000
                                              
```

## 心得
> 以前就有學過選擇權模型，這次的練習讓我比之前更熟練一些~
