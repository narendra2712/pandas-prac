'''name = "narendra"
print("my name is {}".format(name))
print(f"I am {name}")'''
'''from datetime import datetime
today = datetime(year=2024, month=4 , day=30)
print(f"{today:%B %d , %Y , %w}")
#print(today)'''
#-----------------------------------------------------------------------------------------------

#reading pdf using python

'''
import PyPDF2
file =open("pybook.pdf", mode="rb")
reader=PyPDF2.PdfReader(file)
print(len(reader.pages))
pageone=reader.pages[1]
print(pageone.extract_text())
file.close()
'''


#Identifiers and quantifiers for re
import re
'''
text = "call to 9502224640"
#pattern=r'\d\d\d\d\d\d\\d\'
pattern =r'\d{10}'#quantifier
number=re.search(pattern,text)
print(number.group())
print(number.span())
print(number)
#----------------------------------------------------------------------------------------
import re
text = "call to 950-222-4640"
#pattern=r'\d\d\d\d\d\d\\d\'
pattern =r"(\d{3})-(\d{3}-)(\d{4})"#quantifier
number=re.search(pattern,text)
print(number.group(0))
print(number.group(1))
print(number.group(2))
#Here in re groups indexing starts as 1
#----------------------------------------------------------------------------------------

#pipeing
op=re.search(r'man|woman', "He is a man")
pp=re.search(r'man|woman', "He is a woman")
print(op)
print(pp)
#wilcardchr
wlc=re.findall(r'.an',"Man can ban a fan")
wlc1=re.findall(r'..an',"Man can ban a afgan fan")
wlc2=re.findall(r'...an',"Man can ban a afgan fan")
print(wlc)
print(wlc1)
print(wlc2)

dlr=re.findall(r'\d{5}$', "please find the number 23445")
dlr2=re.findall(r'\d$', "please find the number 23445")
print(dlr)
print(dlr2)'''

#exclude pattern
exld=re.findall(r'[^\d]', "there are 23 lions in 45 forests")
exld1=re.findall(r'[^\d]+', "there are 23 lions in 45 forests")
print(exld)
print(exld1)

testphrase="I am narendra. where am I? coming from!$#"
list=re.findall(r'[^!@#$.?]+', testphrase)
list1=''.join(list)
print(list1)