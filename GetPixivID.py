#Version Time 22:30~02:00
"""Time 02:22 
bug:总是将某个字符识别为数字1
fix:将前面整体一起截图。ID:xxxxxxxx
   Time 02:47
bug:还是识别为数字1
fix:将数字筛选前的字符存储，如果当中没有字符'I'+'D'就代表识别有误，
将最终数字列表首字符删除就行(大概吧:)"""
import pytesseract
import os
from PIL import Image
from PIL import ImageGrab
from PIL import ImageShow

# pixiv图片ID网页
pix_url = "https://www.pixiv.net/artworks/"
numbers = []
orgn_numbers = " "

# 定义截图的像素位置
Left_PIXEL = 1000
Upper_PIXEL = 770
Right_PIXEL = 1250
Lower_PIXEL = 810
# 截图位置错误时，修改像素位置后的错误次数
loop_errors = 4


# 截图获得pixiv图片ID区域后存储为ID.jpg
def get_Image_ID(left,upper,right,lower):
    getImage = ImageGrab.grab(bbox=(left, upper, right, lower))
    getImage.show()
    getImage.save("ID.jpg")


# 识别图中的ID数字后存储在列表中
def Image_OCR():
    global numbers
    global orgn_numbers
    numbers.clear()
    image = Image.open("ID.jpg")
    code = pytesseract.image_to_string(image)
    for i in code:
        orgn_numbers += i
        if i.isdigit():
            numbers.append(i)


#更改像素位置并
def ChangePIXEL():
# 当捕捉不到ID数字时，变更截图的像素位置。
    global Left_PIXEL,Upper_PIXEL,Right_PIXEL,Lower_PIXEL
    Left_PIXEL -= 22
    Upper_PIXEL -= 2
    Right_PIXEL += 2
    Lower_PIXEL += 2

# 捕捉数字小于pixiv图片id时，循环更改捕捉位置
while len(numbers) < 8:
    get_Image_ID(Left_PIXEL,Upper_PIXEL,Right_PIXEL,Lower_PIXEL)
    Image_OCR()
    #print(orgn_numbers)
    #print(numbers)
    ChangePIXEL()
    loop_errors -= 1
    if loop_errors == -1:
        print('保险退出')
        exit(0)

print(orgn_numbers)
if "ID:" not in orgn_numbers:
    numbers.remove('1');
print(numbers)

# 拼接pixiv网页
for n in numbers:
    pix_url += n

answer = input("是否打开浏览器? ")
if answer == 'y':
    os.system('firefox ' + pix_url)
    os.system('exit')
print(pix_url)
