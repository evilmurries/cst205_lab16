# Lab16 - Team 10
# M. Mariscal, C. Piwarski, W. Robleh
# Developed with Python3.7.1

################################################################################
# 1. Choose a website that you frequent that has data (text) that could be 
# scraped from it's HTML (this could be ABC news, BBC news, Google news, 
# for example)
#
# 2. Write some code that collects at least 10 pieces of information from the 
# webiste (e.g. friends from Facebook, or headlines from CNN, comments on kitty
# pictures, etc)
#
# 3. Create a new web page that displays ONLY the information you collected in 
# step 2
################################################################################


import urllib.request
import os
import re

# This function assembles a new HTML document with the supplied information
def makePage(events):
    filename = 'newPage.html'
    file = os.path.join(os.getcwd(), filename)
    header = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transition//EN"\
 "http://www.w3.org/TR/html4/loose.dtd">'
    title = '<html>\n<head><title> Python Events </title>\n</head>'
    bodyOpen = '<body>\n<h1>'
    bodyClose = '</body>\n</html>'
    try:
        with open(file, 'w') as htmlPage:
            htmlPage.write(header)
            htmlPage.write(title)
            htmlPage.write(bodyOpen)
            htmlPage.write('Upcoming Python Conventions<br>')
            for event in events:
                htmlPage.write(event + '<br>')

            htmlPage.write(bodyClose)
            htmlPage.close()
    except IOError:
        print('Error Creating HTML File. Aborting...')

# Main function for the program
def main():

    # declare variables
    URL = 'https://www.python.org'
    HEADERS = {'User-Agent': "Mozilla/4.0"}
    regex = re.compile(r'<a href="/events/python-events/7.*?">(.*?)</a></li>')

    # open webpage
    try:
        request = urllib.request.Request(URL, headers=HEADERS)
        web_page_request = urllib.request.urlopen(request)
        web_page = web_page_request.read()
        web_page = web_page.decode(encoding='utf-8')
    except Exception as e:
        print('Error has occurred, program ending. Error data is as follows:')
        print(str(e))
        raise SystemExit

    # collect information
    events = regex.findall(web_page)

    # make new page
    makePage(events)

if __name__ == '__main__':
    main()