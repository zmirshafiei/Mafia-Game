import random
import sys
roles = ['پدر خوانده', 'دکتر لکتر', 'مافیا ساده1', 'مافیا ساده2', 'دکتر', 'روانپزشک', 'کاراگاه', 'شهردار', 'حرفه ای', 'جان سخت', 'شهروند ساده1', 'شهروند ساده2']
selection = random.shuffle(roles)

# تعریف متغیر جهت نگهداری محتوای فایل خروجی
output = ""

# متغیر نگهدارنده لیست شرکت کنندگان به همراه نقش ها
participant_list = {}

# متغیر تعداد شرکت کنندگان
round_count = 0

try:
    round_count = int(input("تعداد افراد شرکت کننده را وارد کنید:\n"))
    if round_count < 9:
        print("تعداد شرکت کنندگان نباید کمتر از 9 باشد")
        sys.exit()
except:
    print("تعداد شرکت کنندگان باید یک عدد صحیح باشد.")
    sys.exit()
round = 0
while round < round_count:
    # نمایش یک ورودی برای گرفتن نام شرکت کنندگان. round+1 برابر است با شماره شرکت کنندگان که از 1 شروع میشود.
    participant = input('نام شرکت کننده '+str((round+1))+' را وارد کنید\n ')
    participant_list[participant] = roles[round]
    round = round + 1

# اضافه کردن اولین خط به متغیر output برای فایل خروجی 
output += "شرکت کننده = نقش:\n"

# گرفتن یک لوپ از آیتم های دیکشنری participant_list
for name, role in participant_list.items():
    # اضافه کردن شرکت کنندگان و نقش ها به خطوط متغیر output
    output += name+" "+role+"\n"

# تعریف متغیر حاوی کارت های بازی
cardes = ["مسیر سبز", "فرش قرمز", "ذهن زیبا", "دروغ سیزده", "بیخوابی", "شلیک نهایی"]
# بُر زدن مقادیر جهت تصادفی شدن متغیر
random.shuffle(cardes)
# اضافه کردن خط "کارت ها" به متغیر output
output += "کارت ها:\n"

# گرفتن لوپ از کارت های بازی
for carde in cardes:
    # اضافه کردن شماره کارت ها و اسامی آنها به متغیر output
    output += str(cardes.index(carde)+1)+" "+carde+"\n"

# تعریف یک نام برای فایل خروجی
filename = "mafia.txt"

# باز کردن فایل خروجی در حالت نوشتاری و با انکودینگ utf-8
with open(filename, "w", encoding="utf-8") as f:
    # نوشتن متغیر output در فایل باز شده
    f.write(output)
