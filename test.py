print("hello essam")
x = 10 
x += 10
x -= 5
print(x)
range(5)
print(list(range(5)))
name ="my name : {a} age {b} adn fullname {c:.3f}".format(a="essam", b=24 , c=1.2324233334)
print(name)
name1 = "moahmed"
age= 24 
full ="moamedessam"

fullname = f"myName : {name1}, age {age}, gullname {full}"
print(fullname)


# def sum_pairs_before(numbers):
#     results = []
#     for i in range(2, len(numbers)):
#         current_sum = numbers[i-2] + numbers[i-1]
#     results.append(current_sum)
# return results


files = "txts.txt"
#         # خليهم يبدأوا من أول السطر تماماً بدون مسافات في البداية
# with open (files) as file:
# content = file.read()
# print(content.rstrip())

# with open (files) as filess:
#     lcounter = 1
#     for line in filess:
#         print(lcounter, line.rstrip())
#         lcounter  += 1

# الطبقة 0: (على الحيطة خالص بره)


# الطبقة 0: البوابة الأولى بتبدأ من أول السطر خالص
with open(files, "a") as files_object:
    # الطبقة 1: دخلنا جوة الـ with (اضغط Tab واحدة)
    add_line = files_object.write(" hi am mohamed essam2 \n ") 

# الطبقة 0: رجعنا تاني بره خالص عشان نفتح البوابة الثانية
with open(files, "r") as object_files2:
    # الطبقة 1: دخلنا جوة الـ with الثانية (اضغط Tab واحدة)
    count = 1
    content_file = object_files2.readlines()
    
    # الطبقة 1: الـ for نفسها جوا الـ with فتأخد (Tab واحدة)
    for all_lines in content_file:
        # الطبقة 2: السطور دي جوه الـ for وجوه الـ with (اضغط 2 Tab)
        print(count, all_lines.rstrip())
        count += 1