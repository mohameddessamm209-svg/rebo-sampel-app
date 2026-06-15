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

with open (files) as filess:
    lcounter = 1
    for line in filess:
        print(lcounter, line.rstrip())
        lcounter  += 1