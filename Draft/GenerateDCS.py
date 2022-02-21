import string

from string import Template
a = "name"
tempTemplate = string.Template("Hello $name ,your website is $message")
print(tempTemplate.safe_substitute(name='大CC', message='http://blog.me115.com'))
s = Template('There  ${moneyType} is  ${money}')
print(s.safe_substitute(moneyTypes = 'Dollar'))
tempTemplate = Template("There $a and $b")
d={'a':'apple','b':'banbana'}