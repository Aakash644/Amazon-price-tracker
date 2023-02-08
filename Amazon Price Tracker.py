# library files 
import smtplib
from bs4 import BeautifulSoup
import requests  
#headers for http get method goto http://myhttpheader.com/ to get your browser Headers
headers={
    "Accept-Language":"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}  
# this url belongs to baot rockerz neckband that i wanted to buy 
try:
    url="https://www.amazon.in/Airdopes-141-Bluetooth-Wireless-Playtime/dp/B09N3XMZ5F/ref=sr_1_1_sspa?crid=1I0BDW8RNGUQ1&keywords=boat+earbuds&qid=1675852498&s=electronics&sprefix=boat%2Celectronics%2C779&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
    response=requests.get(url=url,headers=headers) 
    response.raise_for_status 
    # creating an object of beautifulsoup class 
    soup=BeautifulSoup(response.text,"html.parser")    
    # using find method to find the price of favourite product
    data=soup.find("span",{"class":"a-price-whole"})  
    #using split function to remove ₹ sign 

    x=data.text.split(",") 

    original_price=float("".join(x)) 
    
    title=soup.find(name="span",id="productTitle").text  
    
    if(original_price<=1200):  
       password="zdqrciuwtznqtqvh" 
       email="aakashkumar6789655@gmail.com" 
       connection=smtplib.SMTP("smtp.gmail.com")
       connection.starttls()
       connection.login(user=email,password=password)
       connection.sendmail(from_addr=email,to_addrs="aakshkr10@gmail.com",msg=f"Subject:Amazon Price tracker \n\nHurry,Your favourite product is now available at less price.\n Product:{title}\n Price: {original_price}\n Link:{url}")
       connection.close() 
except: 
    password="zdqrciuwtznqtqvh" 
    email="aakashkumar6789655@gmail.com" 
    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=email,password=password)
    connection.sendmail(from_addr=email,to_addrs="aakshkr10@gmail.com",msg=f"Subject:Oops!  \n\nThe given Url does not exist. Please check the Given url and try again.")
    connection.close() 

