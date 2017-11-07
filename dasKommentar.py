#!/usr/bin/env python3

'''The purpose of this script is to extract developer comments from a webpage.  This Python script can be used
by everyone from Web Pentesters, Red Teams, HTML developers, to generally nosy Gladys Kravitz types.  
Why? Because sometimes devs don't do a good job cleaning up their code and leave behind helpful clues that can 
be leveraged into additional misdeeds. The idea for this came from HackThisSite's Realistic Challenge 3.

Please be aware, this script does not replace diligent HTML code source review, just merely acts as a 
"double check" in case something of interest is overlooked.  

This script depends on BeautifulSoup to run.

This Python script was written by James Russell.
'''


from bs4 import BeautifulSoup
from bs4 import Comment
from pathlib import Path
import requests
import sys


#including a user agent string.  I don't think it matters (I did not run into any problems without it), but
#I figured why not.  Feel free to comment it out and make the apporporate update to the Process block.
user_agent = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0'}



def process(url):
    page  = requests.get(url, headers=user_agent)
    data = page.text


    print("")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")

    soup=BeautifulSoup(data,'html.parser')

    for comments in soup.findAll(text=lambda text:isinstance(text,Comment)):
        print("")
        print("")
        print(comments)
        print("")
        print("")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("")



def main():
    if len(sys.argv) == 1:
        print("Usage: ./{0} http://www.example.com".format(Path(sys.argv[0]).name))
        sys.exit(1)
        
    for url in sys.argv[1:]:
        process(url)
    
    

if __name__ == "__main__":
    main()    