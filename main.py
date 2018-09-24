import sys
import smtplib
import time
from selenium import webdriver
from selenium.webdriver import Chrome

url1 = """https://service.berlin.de/terminvereinbarung/termin/tag.php?
          id=&buergerID&buergername=&absagecode=&Datum=1441058400&anliegen%5B%5D=120686&
          dienstleister%5B%5D=122210&dienstleister%5B%5D=122217&
          dienstleister%5B%5D=122219&dienstleister%5B%5D=122227&
          dienstleister%5B%5D=122231&dienstleister%5B%5D=122238&
          dienstleister%5B%5D=122243&dienstleister%5B%5D=122252&
          dienstleister%5B%5D=122260&dienstleister%5B%5D=122262&
          dienstleister%5B%5D=122254&dienstleister%5B%5D=122271&
          dienstleister%5B%5D=122273&dienstleister%5B%5D=122277&
          dienstleister%5B%5D=122280&dienstleister%5B%5D=122282&
          dienstleister%5B%5D=122284&dienstleister%5B%5D=122291&
          dienstleister%5B%5D=122285&dienstleister%5B%5D=122286&
          dienstleister%5B%5D=122296&dienstleister%5B%5D=150230&
          dienstleister%5B%5D=122301&dienstleister%5B%5D=122297&
          dienstleister%5B%5D=122294&dienstleister%5B%5D=122312&
          dienstleister%5B%5D=122314&dienstleister%5B%5D=122304&
          dienstleister%5B%5D=122311&dienstleister%5B%5D=122309&
          dienstleister%5B%5D=317869&dienstleister%5B%5D=324433&
          dienstleister%5B%5D=325341&dienstleister%5B%5D=324434&
          dienstleister%5B%5D=122281&dienstleister%5B%5D=122276&
          dienstleister%5B%5D=122274&dienstleister%5B%5D=122267&
          dienstleister%5B%5D=122246&dienstleister%5B%5D=122251&
          dienstleister%5B%5D=122257&dienstleister%5B%5D=122208&
          dienstleister%5B%5D=122226&herkunft=http://service.berlin.de/dienstleistung/120686/"""
url2 = """https://service.berlin.de/terminvereinbarung/termin/tag.php?
          id=&buergerID=&buergername=&absagecode=&Datum=1443650400&anliegen%5B%5D=120686&
          dienstleister%5B%5D=122210&dienstleister%5B%5D=122217&
          dienstleister%5B%5D=122219&dienstleister%5B%5D=122227&
          dienstleister%5B%5D=122231&dienstleister%5B%5D=122238&
          dienstleister%5B%5D=122243&dienstleister%5B%5D=122252&
          dienstleister%5B%5D=122260&dienstleister%5B%5D=122262&
          dienstleister%5B%5D=122254&dienstleister%5B%5D=122271&
          dienstleister%5B%5D=122273&dienstleister%5B%5D=122277&
          dienstleister%5B%5D=122280&dienstleister%5B%5D=122282&
          dienstleister%5B%5D=122284&dienstleister%5B%5D=122291&
          dienstleister%5B%5D=122285&dienstleister%5B%5D=122286&
          dienstleister%5B%5D=122296&dienstleister%5B%5D=150230&
          dienstleister%5B%5D=122301&dienstleister%5B%5D=122297&
          dienstleister%5B%5D=122294&dienstleister%5B%5D=122312&
          dienstleister%5B%5D=122314&dienstleister%5B%5D=122304&
          dienstleister%5B%5D=122311&dienstleister%5B%5D=122309&
          dienstleister%5B%5D=317869&dienstleister%5B%5D=324433&
          dienstleister%5B%5D=325341&dienstleister%5B%5D=324434&
          dienstleister%5B%5D=122281&dienstleister%5B%5D=122276&
          dienstleister%5B%5D=122274&dienstleister%5B%5D=122267&
          dienstleister%5B%5D=122246&dienstleister%5B%5D=122251&
          dienstleister%5B%5D=122257&dienstleister%5B%5D=122208&
          dienstleister%5B%5D=122226&herkunft=http://service.berlin.de/dienstleistung/120686/"""

xpath_termin1 = """//*[@id="hhibody"]/div[3]/div[2]/div[1]/div[2]/div[%d]/table/tbody/tr[%d]/td[%d]/a"""
xpath_month = '''//*[@id="hhibody"]/div[3]/div[2]/div[1]/div[2]/div[%d]/table/thead/tr[1]/th[2]/text()'''
xpath_date = '''//*[@id="hhibody"]/div[3]/div[2]/div[1]/div[2]/div[%d]/table/tbody/tr[%d]/td[%d]/a/u/span'''
timeout = False

def send_email(month, date):

    fromaddr = 'from_address'
    toaddrs = 'to_address'
    msg = """There is an appointment, here is the link %s'""" % (url1)

    username = ''
    password = ''

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()


driver = webdriver.Chrome()
driver.get(url2)
driver.implicitly_wait(0)

assert "Terminvergabe" in driver.title

print 'Browser open'

while timeout is False:
    driver.refresh()
    time.sleep(5)

    for x in range(1, 3):

        for i in range(1, 5):

            for j in range(1, 8):

                exception = 0

                try:
                    termin_link = driver.find_element_by_xpath(xpath_termin1 % (x, i, j))

                except:
                    exception = 1

                if exception == 1:
                    exception == 1
                else:
                    #print 'Nothing happened'

                    termin_link.click()

                    month = 'Not yet'

                    date = 'Not yet'

                    send_email(month, date)

                if exception == 0:
                    timeout = True

                #print str(x) + ' ' + str(i) + ' ' + str(j)
                #print xpath_termin1 % (x, i, j) + '--Exception ' + str(exception)

    time.sleep(5)
driver.close()

print x, i, j

