from PIL import Image, ImageDraw, ImageFont, ImageFilter


# 实例一个图片对象300*60
width = 60 * 5
heiht = 60
# 图片颜色
clo = (43, 34, 88)  # 我觉得是紫蓝色
image = Image.new('RGB', (width, heiht), clo)
# 创建Font对象
font = ImageFont.truetype('./ukai.ttc', 36)

# 创建Draw对象
draw = ImageDraw.Draw(image)

# 输出文字
str1 = "ren ren Python"
w = 4  # 距离图片左边距离
h = 10  # 距离图片上边距离
draw.text((w, h), str1, font=font)
# 模糊
image.filter(ImageFilter.BLUR)
code_name = 'test_code_img.jpg'
save_dir = './{}'.format(code_name)
image.save(save_dir, 'jpeg')
print("已保存图片：{}".format(save_dir))
