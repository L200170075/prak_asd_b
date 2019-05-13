import re

print ('no 1')
f = open('Indonesia.txt', 'r')
p = r'\s[Dd]i\w+'
string = re.findall(p, f.read())
print (string)
