i = 1
while i <= 9:
    j = 1
    while j <= i:
        result = j * i
        print(j,'×',i,'=',result,'  ',end = '')
        #print('%2d*%2d = %2d'%(j,i,result),' ',end = '')
        j += 1
    i += 1
    print()
