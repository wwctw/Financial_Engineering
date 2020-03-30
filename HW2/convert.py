# -*- coding: utf-8 -*-

import math

m1 = float(input("   請輸入轉換前每年期數 若為連續期數請輸入 0 :  "))
r1 = float(input("   請輸入轉換前年利率(%) :  "))
m2 = float(input("   請輸入轉換後每年期數 若為連續期數請輸入 0 :  "))

r1 = r1/100
if (m1 > 0.0) and (m2 > 0.0):
    r2 = ( ( 1 + r1/m1 )**( m1/m2 ) - 1 ) * m2
elif (m1 > 0.0) and (m2 == 0.0):
    r2 = m1 * math.log( 1 + r1/m1 )
elif (m1 == 0.0) and (m2 > 0.0):
    r2 = m2 * ( math.exp( r1/m2 ) - 1 )
elif (m1 == 0.0) and (m2 == 0.0):
    r2 = r1
r2 = r2*100

print("\n   轉換後的年利率為",'%8.3f'%r2,"%\n")

