import os

# 164
# age = int(input('please specify age:'))
# name_list = []
# mylist = os.listdir('python_daser/BabyNames')
# try:
#     with open(f'python_daser/BabyNames/{age}_BoysNames.txt', 'r') as file1, \
#          open(f'python_daser/BabyNames/{age}_GirlsNames.txt', 'r') as file2:
#          for line1, line2 in zip(file1, file2):
#             name_list.append(line1.split(' ')[0])
#             name_list.append(line2.split(' ')[0])
# except FileNotFoundError:
#     print("File not found")
# print(name_list if name_list else "Empty List")

# 166
# count = 1900
# men_list = []
# girl_list = []
# mylist = os.listdir('python_daser/BabyNames')
# try:
#     while True:
#         with open(f'python_daser/BabyNames/{count}_BoysNames.txt', 'r') as file1, \
#              open(f'python_daser/BabyNames/{count}_GirlsNames.txt', 'r') as file2:
#                 count += 1
#                 if count == 2012:    
#                     break
#                 for l in file1:
#                     men_list.append(l.split(' ')[0])
#                 for j in file2:
#                     girl_list.append(j.split(' ')[0])

                
# except FileNotFoundError:
#     print("File not found!")
# print(set(men_list))
# print(set(girl_list))

