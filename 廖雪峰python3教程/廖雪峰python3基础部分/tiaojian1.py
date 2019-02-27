# -*- coding: utf-8 -*-
height = float(input('请输入您的身高：'))
weight = float(input("请输入您的体重："))
bmi = weight / pow(height, 2)
height_str = "您的身高为：%.2f M"
weight_str = "您的体重为：%.2f KG"
bmi_str = "您的BMI指数为 %.2f %s"
print(height_str % height)
print(weight_str % weight)
if bmi < 18.5:
    print(bmi_str % (bmi, "过轻"))
elif 18.5 <= bmi < 24:
    print(bmi_str % (bmi, "正常"))
elif 24 <= bmi < 27:
    print(bmi_str % (bmi, "过重"))
elif 27 <= bmi < 30:
    print(bmi_str % (bmi, "肥胖"))
elif 30 <= bmi < 35:
    print(bmi_str % (bmi, "中度肥胖"))
elif bmi > 35:
    print(bmi_str % (bmi, "严重肥胖"))