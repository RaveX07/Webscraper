from selenium import webdriver
import time
import smtplib

driver = webdriver.Firefox()
link = "https://www.amazon.de/Neues-Apple-iPhone-Pro-128-GB/dp/B08L5SNWD2/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=iphone+12+pro&qid=1605195325&sr=8-5"
driver.get("https://www.amazon.de/Neues-Apple-iPhone-Pro-128-GB/dp/B08L5SNWD2/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=iphone+12+pro&qid=1605195325&sr=8-5")

def sendemail():
    global pricetext
    EMAIL_ADDRESS = "jannisschroter@gmail.com"
    EMAILS_PASSWORD = "Jann1s2007"
    msg = """\
        Das iPhone kostet unter 1100 Euro
        Das war das Python Skript von Jannis
    """

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAILS_PASSWORD)
    print("Login succes")
    server.sendmail(EMAIL_ADDRESS, "schroeter1102@web.de", msg)
    print("Email erfolgreich gesendet")


while True:
    price = driver.find_element_by_id("priceblock_ourprice")
    print(price.text)
    komma = price.text.find(",")
    punkt = price.text.find(".")
    punkt1 = punkt + 1
    pricetext = price.text
    price1 = price.text[0]
    prcie2 = price.text[punkt1:komma]
    priceint = price1 + prcie2
    print(priceint)
    if int(priceint) <= 1100:
        sendemail()
        print(f"Das iPhone 12 Pro kostet gerade nur {price.text}")
        break
    driver.refresh()
    time.sleep(60*10)

driver.quit()
