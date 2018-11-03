from PIL import Image, ImageDraw, ImageFont, ImageFilter

# 实例一个图片对象300*60
width = 60 * 5
height = 60
# 图片颜色
clo = (43, 34, 88)
image = Image.new('RGB', (width, height), clo)
# 创建Font
font = ImageFont.truetype('./ukai.ttc', 36)

# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充像素
# 宽每隔20,高每隔5,形成坐标x，y
# 红色：220 20 60
for x in range(0, width, 20):
    for y in range(0, height, 5):
        draw.point((x, y), fill=(200, 20, 60))

str1 = "We are renren"
w = 4  # 距离图片左边距离
h = 10  # 距离图片上边距离
draw.text((w, h), str1, font=font, fill=(78, 64, 65))
# 模糊
image.filter(ImageFilter.BLUR)
code_name = 'test_code_img1.jpg'
save_dir = './{}'.format(code_name)
image.save(save_dir, 'jpeg')
print("已保存图片：{}".format(save_dir))
