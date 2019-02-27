"""
from PIL import Image
# 打开一个JPG图像文件，注意是当前路径：
im = Image.open('KFC1.jpg')
# 获得图像尺寸
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用JPEG格式保存
im.save('thumbnail.jpg', 'jpeg')
# 在IDE中可以看见修改后的图像
im.show()
"""
print('----------------------------------------------')

from PIL import Image, ImageFilter

# 打开一个jpg图像文件，注意是当前路径：
im = Image.open('KFC1.jpg')
# 应用模糊滤镜
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')
im2.show()