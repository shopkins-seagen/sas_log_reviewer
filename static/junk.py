import re

test = 'ERROR 202-322: The option or parameter is not recognized'
x = re.search('^ERROR(:|.*:)',test,re.IGNORECASE)
if (x):
    print(x.group())