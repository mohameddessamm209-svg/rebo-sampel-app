# print("hello essam")
# x = 10 
# x += 10
# x -= 5
# print(x)
# range(5)
# print(list(range(5)))
# name ="my name : {a} age {b} adn fullname {c:.3f}".format(a="essam", b=24 , c=1.2324233334)
# print(name)
# name1 = "moahmed"
# age= 24 
# full ="moamedessam"

# fullname = f"myName : {name1}, age {age}, gullname {full}"
# print(fullname)


# def sum_pairs_before(numbers):
#     results = []
#     for i in range(2, len(numbers)):
#         current_sum = numbers[i-2] + numbers[i-1]
#     results.append(current_sum)
# return results


# files = "txts.txt"
#         # خليهم يبدأوا من أول السطر تماماً بدون مسافات في البداية
# with open (files) as file:
# content = file.read()
# print(content.rstrip())

# with open (files) as filess:
#     lcounter = 1
#     for line in filess:
#         print(lcounter, line.rstrip())
#         lcounter  += 1
import csv 

# csvfile_opject = "csvfile.csv"
# with open(csvfile_opject, "r", newline="") as file_opj:
#     content = csv.DictReader(file_opj)
#     for row in content:
#         print( row["Make"],"  __ :  __ ", row["Colour"])



# add fields in row in csv file 
# create path file 
csvfile_opject = "csvfile.csv"

# with open(csvfile_opject, "a", newline="") as file_opj:
#     # add attribute "a" append  
#     fieldname =["Make","Colour"] 
#     # setname fieldsname row 
#     content = csv.DictWriter(file_opj, fieldnames=fieldname)
#     # use csv 
#     content.writerow({"Make":"essam","Colour":"white"})
#     # add row in fields 
#     print(dir(content))

# # ============================
# import csv

# csvfile = "cars_data.csv"
# fields = ["Make", "Colour"]

# # لستة شايلة قواميس كتير (List of Dictionaries)
# cars_list = [
#     {"Make": "Toyota", "Colour": "White"},
#     {"Make": "Honda", "Colour": "Red"},
#     {"Make": "BMW", "Colour": "Black"}
# ]

# with open(csvfile, "w", newline="") as objectfile:
#     writer = csv.DictWriter(objectfile, fieldnames=fields)
    
#     # 1. بنستخدم الخاصية دي للتأكد من الأعمدة
#     print("الأعمدة المعتمدة هي:", writer.fieldnames)
    
#     # 2. بنكتب الهيدر أول حاجة
#     writer.writeheader()
    
#     # 3. بنكتب اللستة كلها دفعة واحدة بدل سطر سطر!
#     writer.writerows(cars_list)
# ======================================
import csv

# csvfile2 = "cars_data2.csv"
# with open(csvfile2, "r", newline="") as objectfile:
#     reader = csv.DictReader(objectfile)
    
#     for row in reader:
#        print(row["Make"]," -'_'-", row["Colour"])
        # ========================
    


    

# نص JSON معقد ومكتوب على عدة أسطر (بإستخدام Triple Quotes)

json_string = '''{
    "company": "Toyota Motor Corporation",
    "established": 1937,
    "is_active": true,
    "headquarters": {
        "country": "Japan",
        "city": "Toyota, Aichi"
    },
    "popular_models": [
        {
            "name": "Corolla",
            "type": "Sedan",
            "colors": ["White", "Silver", "Black"],
            "safety_rating": 4.8
        },
        {
            "name": "RAV4",
            "type": "SUV",
            "colors": ["White", "Gray", "Blue"],
            "safety_rating": null
        }
    ],
     "popular2_models": [
        {
            "name": "Corolla",
            "type": "Sedan",
            "colors": ["White", "Silver", "Black"],
            "safety_rating": 4.8
        },
        {
            "name": "RAV4",
            "type": "SUV",
            "colors": ["White", "Gray", "Blue"],
            "safety_rating": null
        }
    ]
}'''

import json
# opject_json = json.loads(json_string)
# print(opject_json)

# for key in opject_json["popular2_models"]:
#     print(key["type"],key["name"])
# تمرير loads
opject_loads = json.loads(json_string )
# ثم تمرر dumps
opject_dumps = json.dumps(opject_loads , indent=2)

print(opject_dumps)