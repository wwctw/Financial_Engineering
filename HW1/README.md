# 本金平均攤還試算  R08323002 學習歷程

## 先說程式執行方法

這支程式是用MATLAB寫成的，只要打開MATLAB執行HW1目錄下的m檔案，就可以依程式提示輸入本金、期數、年利率，程式會直接印出計算結果。

## 甚麼是本金平均攤還法

本金平均攤還法和本息平均攤還法為兩種常見的貸款償還辦法，前者即為本次作業實作的項目。

see [參考資料](https://ttc.scu.org.tw/memdca1.htm)

> 本金平均攤還法是將本金平均在貸款期間償還，每期償還的本金均相同，而每期所攤還的利息卻因累積未攤還之本金逐漸減少而減少，因此，每期所攤還的本利和會越來越少。

## 程式流程圖 

<img src="/HW1/flow.png" border="10" />

## 計算細節

總月份數 = 12 * 期數  
平均每月攤還本金 = 本金 / 總月份數 (無條件進位)  
最後一個月本金 = 本金 - ( 總月份數 - 1 ) * 平均每月攤還本金  

每個月的利息計算方法:  
每月攤還利息 = 未攤還本金 * 年利率% / 12  (四捨五入)  
未攤還本金 扣掉 本月攤還本金 即為下個月的 未攤還本金  

全部利息 即 直接將各月利息相加  
本金利息累計 即 將該月(含)前的各月份本金和利息累計加總  

## 執行範例

執行結果和[參考資料](https://ttc.scu.org.tw/memdca1.htm)一模一樣

```
請輸入本金(元): 1234560000
請輸入期數(年): 3
請輸入年利率(%): 11

  本金                 1234560000 元
  期數(年)                      3
  年利率                       11 %
  每月攤還本金           34293334 元
  每月攤還利息          請參考下表
  全部利息              209360796 元

               本金(元)         利息(元)    本金利息累計(元)
  第001期        34293334         11316800         45610134
  第002期        34293334         11002444         90905912
  第003期        34293334         10688089        135887335
  第004期        34293334         10373733        180554402
  第005期        34293334         10059378        224907114
  第006期        34293334          9745022        268945470
  第007期        34293334          9430667        312669471
  第008期        34293334          9116311        356079116
  第009期        34293334          8801956        399174406
  第010期        34293334          8487600        441955340
  第011期        34293334          8173244        484421918
  第012期        34293334          7858889        526574141
  第013期        34293334          7544533        568412008
  第014期        34293334          7230178        609935520
  第015期        34293334          6915822        651144676
  第016期        34293334          6601467        692039477
  第017期        34293334          6287111        732619922
  第018期        34293334          5972755        772886011
  第019期        34293334          5658400        812837745
  第020期        34293334          5344044        852475123
  第021期        34293334          5029689        891798146
  第022期        34293334          4715333        930806813
  第023期        34293334          4400978        969501125
  第024期        34293334          4086622       1007881081
  第025期        34293334          3772267       1045946682
  第026期        34293334          3457911       1083697927
  第027期        34293334          3143555       1121134816
  第028期        34293334          2829200       1158257350
  第029期        34293334          2514844       1195065528
  第030期        34293334          2200489       1231559351
  第031期        34293334          1886133       1267738818
  第032期        34293334          1571778       1303603930
  第033期        34293334          1257422       1339154686
  第034期        34293334           943066       1374391086
  第035期        34293334           628711       1409313131
  第036期        34293310           314355       1443920796

```

## 心得

> 這次除了學到本金攤還方式，也學了怎麼寫Markdown，同時做了個視覺化的流程圖，希望以後能把GitHub經營好~

