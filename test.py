'''
Author: Osman Çakmak
Skype: oxcakmak
Email: oxcakmak@hotmail.com
Website: http://oxcakmak.com/
Country: Turkey [TR]
'''
string = input("Enter String:")
lower = 0
upper = 0
print(string)
for i in string:
    if(i.islower()):
        lower = lower + 1
    elif(i.isupper()):
        upper = upper + 1

print('Lowercase characters: %s' % lower)
print('Uppercase characters: %s' % upper)
