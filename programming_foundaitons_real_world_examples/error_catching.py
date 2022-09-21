""" Error Catching """

""" Trying to Download Things That Don't Exist """

import urllib.request


# urlopen() method returns an HTTP response

try:
    webpage = urllib.request.urlopen('http://www.google.com')
except:
    print('Could not access webpage!') 
else:
    for line in webpage:
        print(line)
