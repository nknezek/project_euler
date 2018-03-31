# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 12:13:59 2015

@author: nknezek
"""
#%%
nums = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',
        8:'eight', 9:'nine', 10:'ten', 20:'twenty', 30:'thirty', 40:'forty',
        50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety',
        11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',
        16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
def num2wd(n):
    n = int(n)
    if n>=10**6 or n<0:
        raise Exception('number out of range 1 to 10^6-1')
    if n>=1000:
        return num2wd(n/1000)+' thousand '+num2wd(n%1000)
    elif n>=100:
        if n%100==0:
            return num2wd(n/100)+' hundred'
        else:
            return num2wd(n/100)+' hundred and '+num2wd(n%100)
    elif n>20:
        return nums[n-n%10]+' '+num2wd(n%10)
    elif n>0:
        return nums[n]
    elif n==0:
        return ''
    else:
        raise Exception('number out of range 1 to 10^6-1')

length = 0
for n in range(1,1001):
    length += len(num2wd(n).replace(' ',''))