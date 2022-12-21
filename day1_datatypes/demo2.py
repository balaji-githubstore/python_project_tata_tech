# import demo1
""" advance datatypes """
import math

print(math.pi)



my_name = "balaji@dinakaran"
list=my_name.split("@")
print(list)
print(list[0])
print(list[1])
print(list[0].title()+list[1].title())



print(my_name.title())

print(my_name.capitalize())

print(my_name)
print(my_name[5])
print(len(my_name))

print(my_name.upper())
print(my_name.lower())
print(my_name)
print(type(my_name))

colors = ["red", "green", "yellow", "blue", "green"]

index_of_green = colors.index("green")
colors.insert(index_of_green, "blue")
colors.remove("green")

print(len(colors))
print(type(colors))

print(colors[0])
print(colors[1])

print(colors)

colors.append('orange')

print(colors)

colors.remove("green")
print(colors)

print(colors[1])
colors.remove(colors[1])

print(colors)

# insert violet at index 0
colors.insert(0, "violet")

print(colors)

print(len(colors))

colors.append("red")

print(colors)

print(colors.count("orange"))

print(colors)
value = colors.pop(0)

print(colors)
print(value)

signals = ("red", "green", "yellow")

print(signals)
print(type(signals))

print(signals[0])

appium_dic = {
    "platformName": "android",
    "deviceName": "oneplus",
    "browserName": "chrome",
    "deviceId": 788787
}

print(type(appium_dic))

print(appium_dic['deviceId'])
print(appium_dic["deviceName"])

student_record = {
    'studentId': 101,
    'studentName': 'john',
    'percentage': 78.2,
    'marks': [88, 65, 78, 77, 99],
    'subjects': ['English', 'Social'],
    'sports': {"indoor": "chess", "outdoor": "football"}
}
print(student_record)

print(student_record['percentage'])

print(student_record['marks'])

print(student_record['marks'][4])
print(student_record['subjects'])

print(student_record['sports']['indoor'])

student_record1 = {
    'studentId': 101,
    'studentName': 'john',
    'percentage': 78.2,
    'marks': [88, 65, 78, 77, 99],
    'subjects': ['English', 'Social'],
    'sports': {"indoor": "chess", "outdoor": "football"}
}

student_record2 = {
    'studentId': 102,
    'studentName': 'john',
    'percentage': 78.2,
    'marks': [88, 65, 78, 77, 99],
    'subjects': ['English', 'Social'],
    'sports': {"indoor": "chess", "outdoor": "football"}
}


students=[student_record1,student_record2]

print(students[1]['studentId'])

a=True


