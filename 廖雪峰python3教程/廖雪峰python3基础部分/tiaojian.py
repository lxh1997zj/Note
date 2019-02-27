# -*- coding: utf-8 -*-
height = 1.75
weight = 80.5
bmi = weight/(height*height)
if bmi > 32:
    print('your bmi is %.2f,严重肥胖！'%bmi)
elif bmi > 28:
    print('your bmi is %.2f,肥胖！'%bmi)
elif bmi > 25:
    print('your bmi is %.2f,过重！'%bmi)
elif bmi >= 18.5:
    print('your bmi is %.2f,正常！'%bmi)
else:
	print('your bmi is %.2f,过轻！'%bmi)