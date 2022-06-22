from cmath import log
from http.server import executable
from wsgiref import headers
from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
from .models import Item
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from apscheduler.schedulers.background import BackgroundScheduler

# Create your views here.
from selenium.webdriver import Chrome
# driver = Chrome(executable_path = 'chromedriver')
# driver.get('https://www.myntra.com/casual-shoes/red-tape/red-tape-women-white-sneakers/17301784/buy/js')
# soup = BeautifulSoup(driver.page_source,'lxml')
# price_span = soup.find("span", class_="pdp-offers-price")
# print(price_span)

def index(request):
    return render(request,'main_app/search.html')

@login_required
def search(request):
    if request.method == "POST":

        item_url = request.POST.get("searchbox")
        maximum_price = int(request.POST.get("max_price"))

        if item_url !="" and maximum_price!= "":
            user = request.user
            item_model = Item(user = user, url = item_url, max_price = maximum_price)
            item_model.save()
            
            return redirect('search')
    
    return render(request,'main_app/search.html')
        


def search_price():
    # max_price = 2000000
    hdr = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36" }
    
    for element in Item.objects.all():
        if element.status == False:
            user = element.user
            user_email = user.email
            item_url = element.url
            max_price = element.max_price

            url = requests.get(str(item_url),headers = hdr)
            soup = BeautifulSoup(url.content,'html5lib')
            title = soup.title
            print(title.text[:15])

            price_span = soup.find('div', class_="_30jeq3 _16Jk6d").text[1:].split(',')
            # css-901oao r-cqee49 r-1vgyyaa r-1rsjblm
            
            price = int("".join(price_span))
            print("the price is ",price)

            if( price < max_price):
                subject = 'Your product price has reduced'
                message = f"HI {user.username} , your product {item_url}, that you set to track has now reduced to {price}"
                email_from = settings.EMAIL_HOST_USER 
                recipient_list = [user_email]
                send_mail(subject,message,email_from,recipient_list)
                print("mail send")
                element.status = True
                element.save()

            # print(price)



def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(search_price,'interval', minutes = 0.5)

    scheduler.start()