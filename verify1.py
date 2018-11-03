from PIL import Image

im = Image.open("code.jpg")
# (将图片转换为8位像素模式)
im = im.convert("P")

# 打印颜色直方图
print(im.histogram())
