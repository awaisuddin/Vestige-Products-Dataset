import os      
from bs4 import BeautifulSoup, SoupStrainer
import requests



url = "https://happy-kepler-4b3a61.netlify.app/"



myFile = open("Vestigeproductsdataset.csv", 'w')
myFile.write("Category"+","+"Name"+","+"Price"+","+"Image"+","+"Videolink"+","+"Description"+","+"Reviews")
myFile.close()


            
page = requests.get(url)    
data = page.text
soup = BeautifulSoup(data, 'html.parser')

for link in soup.find_all('a'):

    category = str(link.get('href')).replace("/","")

    categorylink = "https://www.vestproduct.com/"+str(category)+"/?products-per-page=all"

    print(category)
    
    print(categorylink+"-------------------------------------------------------------------------")

    url1 = str(categorylink)
    

    page1 = requests.get(url1)    
    data1 = page1.text
    soup1 = BeautifulSoup(data1, 'html.parser')

    for link1 in soup1.find_all('a'):
        if "woocommerce-LoopProduct-link" in str(link1.get("class")):
            
            print(link1.get("href"))
            links =  str(link1.get("href"))

            url4 = links

            page4 = requests.get(url4)    
            data4 = page4.text
            soup4 = BeautifulSoup(data4, 'html.parser')


            for link4 in soup4.find_all('h2'):
                if "product_title" in str(link4.get("class")):
                    print(link4.get_text())
                    name = str(link4.get_text()).replace(",","")
            for link4 in soup4.find_all('span'):
                if "woocommerce-Price-amount" in str(link4.get("class")):
                    print(link4.get_text())
                    price = str(link4.get_text())
                    break
            for link4 in soup4.find_all('img'):
                if "wp-post-image" in str(link4.get("class")):
                    if "351" in str(link4.get("height")):
                        print(link4.get('src'))
                        img = str(link4.get('src'))
            for link4 in soup4.find_all('iframe'):
                print(link4.get("src"))
                videolink = str(link4.get("src"))
            for link4 in soup4.find_all('div'):
                if "woocommerce-Tabs-panel--description" in str(link4.get("class")):
                    print(link4.get_text())
                    description = str(link4.get_text()).replace(",","")

            for link4 in soup4.find_all('div'):
                if "comment-text" in str(link4.get("class")):
                    print(link4.get_text())
                    reviews = str(link4.get_text()).replace(",","")

            myFile = open("Vestigeproductsdataset.csv", 'a+', encoding='utf-8')
            
            myFile.write("\n"+str(category).replace(",","")+","+str(name)+","+str(price).replace(",","")+","+str(img)+","+str(videolink)+","+str(description)+","+str(reviews))
            
            myFile.close()






            

'''
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
