import math

opty = int(input( \
           "   請輸入計算買權價格或賣權價格  買權請輸入 1  賣權請輸入 2 :  "))
strikeprice = float(input("   請輸入履約價格 :  "))
duration = int(input("   請輸入總期數 :  "))
ccrate = float(input("   請輸入每期連續複利利率(%) :  "))
stocknow = float(input("   請輸入現在股票價格 :  "))
u = float(input("   請輸入次期股票高價與本期價格的比值 :  "))
d = float(input("   請輸入次期股票低價與本期價格的比值 :  "))

R = math.exp(ccrate/100)
p = (R-d)/(u-d)

stockprice = [[stocknow]]
for k in range(1,duration+1):
    stockprice.append([])
    for m in  range(0,k+1):
        stockprice[k].append( \
                   stocknow*math.exp( (k-m)*math.log(u) + m*math.log(d) ) )        

prob = [[1.0]]
for k in range(1,duration+1):
    prob.append([])
    prob[k].append( prob[k-1][0]*p )
    for m in  range(1,k):
        prob[k].append( prob[k-1][m]*p + prob[k-1][m-1]*(1-p) )
    prob[k].append( prob[k-1][k-1]*(1-p) )


optionprice = [ [ 0 for m in range(0,k+1) ] for k in range(0,duration+1) ] 
hedgeratio = [ [ 0 for m in range(0,k+1) ] for k in range(0,duration) ] 

if opty == 1:
    for m in range(0,duration+1):
        optionprice[duration][m] = max(stockprice[duration][m]-strikeprice,0)
    for k in range(duration-1,-1,-1):
        for m in range(0,k+1):
            optionprice[k][m] = \
                        (p*optionprice[k+1][m]+(1-p)*optionprice[k+1][m+1])/R
            hedgeratio[k][m] = ( optionprice[k+1][m]-optionprice[k+1][m+1] ) \
                       / ( stockprice[k+1][m]-stockprice[k+1][m+1] )
elif opty == 2:
    for m in range(0,duration+1):
        optionprice[duration][m] = max(strikeprice-stockprice[duration][m],0)
    for k in range(duration-1,-1,-1):
        for m in range(0,k+1):
            optionprice[k][m] = \
                        (p*optionprice[k+1][m]+(1-p)*optionprice[k+1][m+1])/R
            hedgeratio[k][m] = ( optionprice[k+1][m]-optionprice[k+1][m+1] ) \
                       / ( stockprice[k+1][m]-stockprice[k+1][m+1] )

print("\n\n\n   輸出結果",end="")

print("\n\n   總期數",'%3d'%duration,"期"," R =",'%.3f'%R, \
       " ( 每期連續複利利率",'%.3f'%ccrate,"% )","\n   現在股票價格", \
       '%.3f'%stocknow," u =",'%.3f'%u," d =",'%.3f'%d,end="")

if opty == 1:
    print("\n   履約價格",'%.3f'%(strikeprice), \
           "的買權價格為",'%.3f'%(optionprice[0][0]),end="")
elif opty == 2:
    print("\n   履約價格",'%.3f'%(strikeprice), \
           "的賣權價格為",'%.3f'%(optionprice[0][0]),end="")

print("\n\n   股票價格表 ( 括弧內為機率 )",end="")
print("\n   ",end="")
for m in range(0,duration+1):
    print("      n = ",'%03d'%m,end="")
for k in range(0,duration+1):
    print("\n   ",end="")
    for m in range(0,k):
        print("              ",end="")
    for m in range(k,duration+1):
        print("    ",'%9.3f'%stockprice[m][k],end="")
    print("\n    ",end="")
    for m in range(0,k):
        print("              ",end="")
    for m in range(k,duration+1):
        print("     (",'%5.3f'%prob[m][k],")",end="")

print("\n\n   選擇權價值表 ( 括弧內為避險比率 )",end="")
print("\n   ",end="")
for m in range(0,duration+1):
    print("      n = ",'%03d'%m,end="")
for k in range(0,duration+1):
    print("\n   ",end="")
    for m in range(0,k):
        print("              ",end="")
    for m in range(k,duration+1):
        print("    ",'%9.3f'%optionprice[m][k],end="")
    print("\n    ",end="")
    for m in range(0,k):
        print("              ",end="")
    for m in range(k,duration):
        print("   (",'%7.3f'%hedgeratio[m][k],")",end="")

print("\n")

