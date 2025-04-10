# -*- coding: utf-8 -*-
from datetime import datetime
import random
import string
from io import BytesIO

# PIL就是pillow
from PIL import Image, ImageFont
from PIL import ImageDraw


class ImageCode():
    def rand_color(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return red, green, blue

    def draw_lines(self, draw, num, width, height):
        for i in range(num):
            x1 = random.randint(8, width - 1)
            y1 = random.randint(8, height - 1)
            x2 = random.randint(8, width - 1)
            y2 = random.randint(8, height - 1)
            draw.line(((x1, y1), (x2, y2)), fill=self.rand_color(), width=random.randint(1, 5))

    def get_text(self):
        list = random.sample(string.ascii_letters + string.digits, 4)
        return ''.join(list)

    def draw_verify_code(self):
        # 生成随机字符串
        code = self.get_text()
        print(code)
        width, height = 120, 50
        image = Image.new('RGB', (width, height), "white")
        font = ImageFont.truetype('font/FREESCPT.TTF', 50)
        draw = ImageDraw.Draw(image)
        # 绘制字符串
        for i in range(4):
            draw.text((random.randint(3, 10) + 25 * i, random.randint(1, 2)), text=code[i], font=font,
                      fill=self.rand_color())

        # 绘制干扰线
        self.draw_lines(draw, 4, width, height)

        # image.show()
        return image, code

    def get_code(self):
        image, code = self.draw_verify_code()

        # 创建一个内存二进制流对象（类似临时文件）
        buf = BytesIO()

        # 将 PIL 图像保存到二进制流中，格式为 JPEG
        image.save(buf, format='jpeg')

        # 从二进制流中获取字节数据
        image_b_string = buf.getvalue()

        return code, image_b_string


# ic = ImageCode()
# ic.draw_verify_code()

def model_to_json(result):
    dict = {}
    for k, v in result.__dict__.items():
        if not k.startswith("_sa_"):
            if isinstance(v, datetime):
                v = v.strftime("%Y-%m-%d %H:%M:%S")
            dict[k] = v
    return dict


# ue图片压缩
def compress_image(source, dest, width=1200):
    im = Image.open(source)
    # 获取图片的宽和高
    x, y = im.size
    if x > width:
        # 进行等比例缩放
        ys = int(y * width / x)
        xs = width
        # 调整图片大小
        temp = im.resize((xs, ys), Image.ANTIALIAS)
        temp.save(dest, quality=80)
    else:
        im.save(dest, quality=80)
