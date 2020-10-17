from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

print("*** ONUR AİR TEST YAZILIMI ***\n\n\n")


tc = input("Lütfen geçerli bir TC Kimlik No giriniz: ")


#Website
chrome_browser = webdriver.Chrome()
chrome_browser.get('https://www.onurair.com/')
time.sleep(2)
chrome_browser.maximize_window()

#Nereden (Türkiye)
while True:
    try:
        nereden = chrome_browser.find_element_by_xpath("//*[@id='depPortArea']/label/span[2]")
        nereden.click()
        print("Nereden butonuna basıldı.")
        time.sleep(1)
        nereden_tr = chrome_browser.find_element_by_xpath("/html/body/div[3]/div/span/span/ul/li[2]")
        nereden_tr.click()
        print("Nereden Türkiye seçildi")
        time.sleep(1)
        break

    except:
        print("Nereden butonunda hata tespit edildi")
        # chrome_browser.close()

#Nereye (Kuveyt)
while True:
    try:
        nereye = chrome_browser.find_element_by_xpath("//*[@id='arrPortArea']/div/label/span[2]")
        nereye.click()
        print("Nereye butonuna basıldı")
        time.sleep(1)
        nereye_kw = chrome_browser.find_element_by_xpath("/html/body/div[3]/div/span/span/ul/li[2]")
        nereye_kw.click()
        print("Nereye Kuveyt seçildi")
        time.sleep(1)
        break
    except:
        print("Nereye butonunda hata tespit edildi")
        # chrome_browser.close()

#Gidiş-Dönüş Tek Yön (Tek Yön)
while True:
    try:
        tek_yon = chrome_browser.find_element_by_xpath("//*[@id='radio']/tbody/tr/td[2]/label")
        tek_yon.click()
        print("Tek Yön seçildi")
        time.sleep(1)
        break
    except:
        print("Gidiş-Dönüş Tek Yön seçiminde hata tespit edildi")
        # chrome_browser.close()

#Bilet Bul
while True:
    try:
        devam = chrome_browser.find_element_by_xpath("//*[@id='btnSearch']")
        devam.click()
        print("Devam et butonuna basıldı")
        time.sleep(5)
        break
    except:
        print("Devam et butonuna basılamadı")
        # chrome_browser.close()

#Aylık Görünüm
while True:
    try:
        aylik_gorunum = chrome_browser.find_element_by_xpath("//*[@id='flightGrid0']/div[1]/div[2]")
        aylik_gorunum.click()
        print("Aylık görünüm ekranına geçildi")
        time.sleep(5)
        break
    except:
        print("Aylık görünüm ekranına geçilemedi")
        # chrome_browser.close()

#Ucus Bul
while True:
    try:
        ucus_bul = chrome_browser.find_element_by_name("group0")
        ucus_bul.click()
        print("Ucus bulundu")
        time.sleep(1)
        break
    except:
        print("Ucus bulunamadı")
        # chrome_browser.close()

#Bilete Devam
while True:
    try:
        ucusa_devam = chrome_browser.find_element_by_id("btnContinue")
        ucusa_devam.click()
        print("Bilete devam ediliyor")
        time.sleep(5)
        break
    except:
        print("Devam edilemedi")
        # chrome_browser.close()

#Ucusu Sec
while True:
    try:
        sec_ucus = chrome_browser.find_element_by_name("group0")
        sec_ucus.click()
        print("Ucus secildi")
        time.sleep(3)
        break
    except:
        print("Ucus secilemedi")
        # chrome_browser.close()

#Bilgilere Devam Et
while True:
    try:
        bilgi_devam = chrome_browser.find_element_by_id("btnContinue")
        bilgi_devam.click()
        print("Yolcu bilgileri ekranına geçildi")
        time.sleep(3)
        break
    except:
        print("Yolcu bilgileri ekranına geçilemedi")

#Yolcu Bilgileri Giriş
try:
    unvansec = chrome_browser.find_element_by_xpath("//*[@id='tabPax1']/div/div[2]/span[1]/div/div/div[1]")
    unvansec.click()
    time.sleep(1)
    s2 = chrome_browser.find_element_by_css_selector("#tabPax1 > div > div.adultContentDiv.pass__adult__form > span.form-group.col-lg-2.col-md-2.col-sm-2.col-xs-4.pass__title > div > div > div.selectize-dropdown.single.form-control > div > div:nth-child(2)").click()
    print("Bayan seçildi")
except:
    print("Ünvan seçilemedi")
time.sleep(0.5)
try:
    ad = chrome_browser.find_element_by_name("name1")
    ad.send_keys("FATMA")
    print("Ad girildi")
except:
    print("Ad girilemedi")
time.sleep(0.2)
try:
    soyad = chrome_browser.find_element_by_name("surname1")
    soyad.send_keys("SOYAD")
    print("Soyad girildi")
except:
    print("Soyad girilemedi")
time.sleep(0.2)
try:
    uyruksec = chrome_browser.find_element_by_xpath("//*[@id='nationality1-selectized']")
    uyruksec.click()
    time.sleep(0.2)
    st = chrome_browser.find_element_by_css_selector("#nationalityGroup1 > div > div > div.selectize-dropdown.single.form-control.search > div > div:nth-child(1)").click()
    print("Uyruk seçildi")
except:
    print("Uyruk seçilemedi")
time.sleep(2)
try:
    gn = chrome_browser.find_element_by_xpath("//*[@id='bday_day_1-selectized']")
    gn.click()
    time.sleep(0.2)
    gnsec = chrome_browser.find_element_by_css_selector("#bdateDiv0 > div.form-group.col-lg-2.col-md-3.col-sm-2.col-xs-4.pass__birthday__day > div > div > div.selectize-dropdown.single.form-control.search > div > div:nth-child(1)").click()
    print("Gün seçildi")
    time.sleep(0.2)
    ay = chrome_browser.find_element_by_xpath("//*[@id='bdateDiv0']/div[2]/div/div/div[1]")
    ay.click()
    time.sleep(0.2)
    aysec = chrome_browser.find_element_by_css_selector("#bdateDiv0 > div.form-group.col-lg-2.col-md-3.col-sm-3.col-xs-4.pass__birthday__month > div > div > div.selectize-dropdown.single.form-control.search > div > div:nth-child(5)").click()
    print("Ay seçildi")
    time.sleep(0.2)
    yil = chrome_browser.find_element_by_xpath("//*[@id='bday_year_1-selectized']")
    yil.click()
    time.sleep(0.2)
    yilsec = chrome_browser.find_element_by_css_selector("#bdateDiv0 > div.form-group.col-lg-2.col-md-2.col-sm-2.col-xs-4.pass__birthday__year > div > div > div.selectize-dropdown.single.form-control.search > div > div:nth-child(22)").click()
    print("Yıl seçildi")
    time.sleep(0.2)
except:
    print("Doğum tarihi girilemedi")
time.sleep(0.2)
try:
    chrome_browser.find_element_by_name("natId1").send_keys(tc)
    print("Kimlik numarası girildi")
except:
    print("Kimlik numarası girilemedi")
time.sleep(0.2)
try:
    chrome_browser.find_element_by_name("email0").send_keys("email@gmail.com")
    print("Email girildi")
except:
    print("Email girilemedi")
time.sleep(0.2)
try:
    chrome_browser.find_element_by_name("frst-tel-number0").send_keys("+905306532743")
    print("Telefon numarası girildi")
except:
    print("Telefon numarası girilemedi")
time.sleep(0.2)
try:
    chrome_browser.find_element_by_name("btnSave").click()
    print("Devam ediliyor")
except:
    print("Bilgiler kayıt edilemedi")
time.sleep(3)

#Onay
try:
    chrome_browser.find_element_by_name("addSSRContinueBTn").click()
    print("Onaylandı")
    print("Sistem çalışıyor")
except:
    print("Onaylanamadı")

time.sleep(5)
chrome_browser.close()


