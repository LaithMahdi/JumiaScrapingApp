from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs

def index(request):
    if request.method == 'POST':
        selected_brand = request.POST.get('brand')
        max_price = request.POST.get('maxPrice')
        min_price = request.POST.get('minPrice')
        sort = request.POST.get('order')
    else:
        selected_brand='None'
        max_price=''
        min_price='15'
        sort='None'
    
    brands = get_brands()
    orders=get_orders()
    smartphones = get_smartphones(selected_brand, max_price,min_price,sort)
    length=len(smartphones)

    return render(request, 'index.html', {
        'brands': brands,
        'smartphones': smartphones, 
        'orders':orders,
        'search':{'brand':selected_brand,'max':max_price,'min':min_price,'length':length}
    })


def get_brands():
    URL = "https://www.jumia.com.tn/smartphones/"
    page = requests.get(URL)
    soup = bs(page.content, 'html.parser')
    brands=[]
    
    brands_section = soup.find_all('a', {'class': 'fk-cb -me-start -fsh0'})
    for i in range(len(brands_section)):
        brands.append(brands_section[i].text)  

    return brands

def get_orders():
    orders=["","newest","lowest-price","highest-price","rating"]
    return orders



def get_smartphones(selected_brand,max_price,min_price,sort):
    URL = f"https://www.jumia.com.tn/smartphones/{selected_brand}/?sort={sort}&price={min_price}-{max_price}"
    print("url search : ",URL)

    page = requests.get(URL)
    soup = bs(page.content, "html.parser")
    
    name=soup.find_all("h3",{"class":"name"})
    price=soup.find_all("div",{"class":"prc"})
    image=soup.find_all("img",{"class":"img"})
    link=soup.find_all("a",{"class":"core"})

    smartphones = []
    for i in range(len(name)):
        smartphones.append({'name':name[i].text,'price':price[i].text,'image':image[i].get('data-src'),'link':link[i].get('href')})  

    return smartphones



