# def head(f):
#     try:
#         lines = 0
#         with open(f,'r') as file:
#             fileContent = file.readlines()
#         for fileLine in fileContent:
#             print(fileLine, end='')
#             lines += 1   
#             if lines == 10:
#                 break
#     except FileNotFoundError:
#         print('No File')
    

# f = input('Enter new filename: ')
# head(f)
#============================================================

# def head(f):
#     try:
#         lens = 0
#         upTo = 0
#         go = 0
#         with open(f,'r') as file:
#             fileContent = file.readlines()
#         for i in range(0, len(fileContent)):
#             lens = i
#             print(lens)
#         if lens + 1 < 10: 
#             upTo = 0
#         else:
#             upTo = lens - 9

#         for fileLine in fileContent:
#             if go >= upTo and go <= lens:
#                 print(fileLine, end='')
#             go += 1
#     except FileNotFoundError:
#         print('No file')

# f = input('Enter new filename: ')
# head(f)

