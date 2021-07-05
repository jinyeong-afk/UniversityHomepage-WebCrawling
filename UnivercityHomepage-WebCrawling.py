fromflask import Flask
fromselenium import webdriver
frombs4 import BeautifulSoup
import time
import os

app = Flask(__name__)

@app.route("/craw/<user_id>/<user_pw>")
def craw(user_id,user_pw):
    driver = webdriver.Chrome()
    add = 'https://door.deu.ac.kr/MyPage'

    driver.get(add)


    #로그인
    
    driver.find_element_by_css_selector('body > form > div:nth-child(5) > div:nth-child(5) > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > input').send_keys(user_id)
    driver.find_element_by_css_selector('body > form > div:nth-child(5) > div:nth-child(5) > div > table > tbody > tr:nth-child(2) > td > input').send_keys(user_pw)
    driver.find_element_by_css_selector('body > form > div:nth-child(5) > div:nth-child(5) > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > a').click()
    driver.find_element_by_css_selector("#gnbContent > div > div.t_menu > ol.t_link > li:nth-child(3) > a").click()
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    subjects = soup.select("#wrap > div.subpageCon > div:nth-of-type(3) > div:nth-of-type(3) > table > tbody > tr")
    i = 2
    val = ""
    for sj in subjects:
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        subjects4 = soup.select("#wrap > div.subpageCon > div:nth-of-type(3) > div:nth-of-type(3) > table > tbody")
        val += "<table id=myMember border='5'> <tr> <th></th> <th></th> <th></th> <th></th> <th></th> <th></th> <th></th> </tr>"
        val += str(soup.select("#wrap > div.subpageCon > div:nth-of-type(3) > div:nth-of-type(3) > table > tbody > tr:nth-of-type(" + str(i) + ") > td.tAlignL.pad_10.font_wei_n > a")) + "<br/>"
        time.sleep(2)
        driver.find_element_by_css_selector("#wrap > div.subpageCon > div:nth-child(3) > div:nth-child(3) > table > tbody > tr:nth-child(" + str(i) + ") > td.tAlignL.pad_10.font_wei_n > a").click()
        time.sleep(2)
        i+=1
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        subjects2 = soup.select("#lnbContent > div > div:nth-of-type(3) > ul > li > ul > li:nth-of-type(3) > a")
        time.sleep(0.5)
        driver.find_element_by_css_selector("#lnbContent > div > div:nth-of-type(3) > ul > li > ul > li:nth-of-type(3) > a > span").click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        subjects3 = soup.select("#sub_content2 > div > table > tbody")
        
        for sub3 in subjects3:
            sub = sub3.select('tr')
            str_sub = str(sub)
            str_sub = str_sub[1:]
            str_sub = str_sub[:-1]
            str_sub = str_sub.replace(',', '')
            val += str_sub
            print(sub)
        driver.back()
        driver.back()
        time.sleep(1)
        if(i==len(subjects)-1):
            break
    driver.close()
    return val

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8080')
