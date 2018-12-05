# Lab16 - Team 10
# M. Mariscal, C. Piwarski, W. Robleh
# Developed with Python2 and JES

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


import urllib2

# This function assembles a new HTML document with the supplied information
def makePage(info):
    file = 'C:\\Users\\Public\\newPage.html'
    header = '<!doctype html><html lang="en">'
    file = open(file, 'w')
    file.write(info)
    file.close()

# Main function for the program
def main():

    # declare variables
    url = 'https://news.google.com/?tab=wn&hl=en-US&gl=US&ceid=US:en'

    # open webpage
    try:
        webPage = urllib2.urlopen(url)
        html = webPage.read()
        # There should be a decode statement. Have to figure it out for python2
    except urllib2.HTTPError:
        print 'HTTP Error Detected. Program Ending.'
        raise SystemExit
    except urllib2.URLError:
        print 'URL Error Detected. Program Ending.'
        raise SystemExit

    # collect information

    # make new page
    makePage(html)