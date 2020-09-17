import os      
from bs4 import BeautifulSoup, SoupStrainer
import requests



url = "https://www.vestproduct.com/health-care/?products-per-page=all"

page = requests.get(url)    
data = page.text
soup = BeautifulSoup(data, 'html.parser')


for link in soup.find_all('a'):
    if "woocommerce-LoopProduct-link" in str(link.get("class")):
        
        print(link.get("href"))




''' ?products-per-page=all
for link in soup.find_all('a'):

    pageno = 1

    category = link.get('href').replace("/","")

    categorylink = "https://www.vestproduct.com/"+str(category)+"/"

    print(category)
    i=i+1
    
    print(categorylink+"-------------------------------------------------------------------------")

    while True:
        urllink = categorylink+"page/"+str(pageno)+"/"

        url1 =  urllink
        page1 = requests.get(url1)    
        data1 = page.text
        soup1 = BeautifulSoup(data1, 'html.parser')

        

        myFile = open(str(category)+"-"+str(pageno)+'.html', 'w')
        myFile.write(str(soup))
        myFile.close()

        if pageno== 10:
            break
        pageno = pageno+1
'''
    
    













    #if "https://www.vestproduct.com/" in str(link):
        





'''
for link in soup.find_all('a'):
    if "videos" in str(link.get('href')):
        #print("\n")
        videowebsitelink="https://vidcloud9.com"+str(link.get('href'))
        #print(str(link.get('href')).replace("/videos/","").replace("-","+"))
        
        x = "https://www.google.com/search?sxsrf=ALeKk02TepDzilhakTKiwze2e510Z-l8Mg%3A1593521030145&ei=hjP7Xpa9CMmP4-EPz5K0oAo&q="+str(link.get('href')).replace("/videos/","").replace("-","+")+"+movie+ratings"

        #print(x)

        url1 = x            

        page1 = requests.get(url1)    
        data1 = page1.text
        soup1 = BeautifulSoup(data1, 'html.parser')
        imdb = ""
        rt = ""
        '''
