# phoneDict = dict([
#     (".", "1"),    (",", "11"),  ("?", "111"), ("!", "1111"), (":", "11111"),
#     ("A", "2"),    ("B", "22"),  ("C", "222"),
#     ("D", "3"),    ("E", "33"),  ("F", "333"),
#     ("G", "4"),    ("H", "44"),  ("I", "444"),
#     ("J", "5"),    ("K", "55"),  ("L", "555"), 
#     ("M", "6"),    ("N", "66"),  ("O", "666"),
#     ("P", "7"),    ("Q", "77"),  ("R", "777"), ("S", "7777"), 
#     ("T", "8"),    ("U", "88"),  ("V", "888"),
#     ("W", "9"),   ("X", "99"),   ("Y", "999"), ("Z", "9999"),
#     (" ", "0")
# ])

# text = input("Enter your text: ")

# for i in range(len(text)):
#     tar=text[i].upper() # tar mi hatik
#     print(phoneDict[tar], end ='')




# phoneDict = dict([
#     ("1", ".----"),    ("A", ".-"),                   ("R", ".-."),
#     ("2", "..---"),    ("B", "-..."),  ("J", ".---"), ("S" , '...'),
#     ("3", "...--"),    ("C", "-.-."),  ("K", "-.-"),  ("T" , '-'),
#     ("4", "...."),    ("D", "-.."),  ("L", ".-.."),    ('U' , '..-'),
#     ("5", "....."),    ("E", "."),  ("M", "--"),       ('V' , '...-'),
#     ("6", "-...."),    ("F", "..-."),  ("N", "-."),    ('W' , '.--'),
#     ("7", "--..."),    ("G", "--."),  ("O", "---"),     ('X' , '-..-'),
#     ("8", "---.."),    ("H", "...."),  ("P", ".--."),    ('Y' , '-.--'),
#     ("9", "----."),   ("I", ".."),   ("Q", "--.-"),     ("Z" , '--..'), 
#     ("0", "----")                                         
# ])


# text = input("Enter your text: ")

# for i in range(len(text)):
#      tar=text[i].upper() 
#      print(phoneDict[tar], end ='')



# phoneDict = dict([
#     ("A", "Ньюфаундленд"),                
#     ("B", "Новая Шотландия"),             ("M", "Онтарио"),    ("Y" , 'Юкон'),
#     ("C", "Остров Принца Эдуарда"),       ("N", "Онтарио"),  
#     ("F", "Нью-Брансуик"),                ("P", "Онтарио"),    
#     ("G", "Квебек"),                      ("R", "Манитоба"),       
#     ("H", "Квебек"),                      ("S", "Саскачеван "),    
#     ("J", "Квебек"),                      ("T", "Альберта"),     
#     ("K", "Онтарио"),                     ("V", "Британская Колумбия"),   
#     ("L", "Онтарио"),                     ("X", "Нунавут"),      
#                                           ("X", "Северо-Западные территории")  
# ])
# text = input("Enter your text: ")

# for i in range(len(text)):
#     tar=text[i].upper() 
#     print(phoneDict[tar], end ='')



# phoneDict = dict([
#     ('A', 1),
#     ('E', 1),
#     ('I', 1),
#     ('L', 1),
#     ('N', 1),
#     ('O', 1),
#     ('R', 1),
#     ('S', 1),
#     ('T', 1),
#     ('U', 1),
#     ('D', 2),
#     ('G', 2),
#     ('B', 3),
#     ('C', 3),
#     ('M', 3),
#     ('P', 3),
#     ('F', 4),
#     ('H', 4),
#     ('V', 4),
#     ('W', 4),
#     ('Y', 4),
#     ('K', 5),
#     ('J', 8),
#     ('X', 8),
#     ('Q', 10),
#     ('Z', 10)
# ])

# count = 0
# text = input('enter text: ')
# for i in range(len(text)):
#     count += phoneDict[text[i].upper()]
#     print(count)

x = int(input('enter number :'))
m_dict = dict([
    ("1", "one"),         ("11", "eleven"),    ("30", "thirty"), 
    ("2", "two"),         ("12", "twelve"),    ("40", "forty"),  
    ("3", "three"),       ("13", "thirteen"),  ("50", "fifty"),  
    ("4", "four"),        ("14", "fourteen"),  ("60", "sixty"),
    ("5", "five"),        ("15", "fifteen"),   ("70", "seventiy"),
    ("6", "six"),         ("16", "sixteen"),   ("80", "eighty"),
    ("7", "seven"),       ("17", "seventeen"), ("90", "ninety"),
    ("8", "eight"),       ("18", "eighteen"),  ("100", "one hundred"),
    ("9", "nine"),        ("19","nineteen"),   ("1000", "one thousand"),
    ("10", "ten"),        ("20", "twenty"),    ("1000000", "one million"), ("1000000000", "one billion")
])

# one two three four five six seven eight nine ten eleven twelve
# thirteen forteen fivteen sixteen seventeen eighteen nineteen
# twenty thirty forty fifty sixty eighty ninety
# hundred thousand million billion

# 12
# 99 
# 999 | four hundred fifty six
# 999999 | thousand
# 999999999 | Million
# 999999999999 | Bilion

if x == 100 or x == 1000 or x == 1000000 or x == 1000000000:
    print(m_dict[str(x)])
elif x < 21:
    print (m_dict[str(x)])
elif x > 20 and x < 100:
    #21 - 99
    print(m_dict[str(x)[0]+"0"] + " " + m_dict[str(x)[1]])
elif x < 1000 and x > 100:
    print(m_dict[str(x)[0]] + " hundred " + m_dict[str(x)[1]+"0"] + " " + m_dict[str(x)[2]])
elif x > 1000 and x < 1000000:
    print(m_dict[str(x)[0]] + " thousnd " + m_dict[str(x)[1]] + " hundred " + m_dict[str(x)[2] + "0"] + " " + m_dict[str(x)[3]])
elif x > 1000000 and x < 10000000:
    print(m_dict[str(x)[0]] + " million " + m_dict[str(x)[1]] + " hundred " + m_dict[str(x)[2] + "0"] + " thousand " + m_dict[str(x)[3]] + " hundred " + m_dict[str(x)[4] + "0"] + " " + m_dict[str(x)[4]])   

