from selenium import webdriver
from bs4 import BeautifulSoup
from openpyxl import Workbook,load_workbook
import time
import os
from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/')
def my_form():
    return render_template('conecpy.html')
@app.route('/', methods=['POST'])
def my_form_post():
    variable = request.form['variable']
    return variable

# 크롬 열기
app.run()
driver = webdriver.Chrome()
add = 'https://door.deu.ac.kr/MyPage'

driver.get(add)


#로그인

driver.find_element_by_css_selector('body > form > div:nth-child(5) > div:nth-child(5) > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > input').send_keys('20173171')
driver.find_element_by_css_selector('body > form > div:nth-child(5) > div:nth-child(5) > div > table > tbody > tr:nth-child(2) > td > input').send_keys('qkdls702~')
driver.find_element_by_css_selector('body > form > div:nth-child(5) > div:nth-child(5) > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > a').click()

time.sleep(1)
driver.find_element_by_css_selector("#gnbContent > div > div.t_menu > ol.t_link > li:nth-child(3) > a").click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
subjects = soup.select("#wrap > div.subpageCon > div:nth-of-type(3) > div:nth-of-type(3) > table > tbody > tr")
i = 2
val = ""
results = []
for sj in subjects:
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    subjects4 = soup.select("#wrap > div.subpageCon > div:nth-of-type(3) > div:nth-of-type(3) > table > tbody")
    val += str(soup.select("#wrap > div.subpageCon > div:nth-of-type(3) > div:nth-of-type(3) > table > tbody > tr:nth-of-type(" + str(i) + ") > td.tAlignL.pad_10.font_wei_n > a")) + "<br/>"
    driver.find_element_by_css_selector("#wrap > div.subpageCon > div:nth-child(3) > div:nth-child(3) > table > tbody > tr:nth-child(" + str(i) + ") > td.tAlignL.pad_10.font_wei_n > a").click()
    i+=1
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    subjects2 = soup.select("#lnbContent > div > div:nth-of-type(3) > ul > li > ul > li:nth-of-type(3) > a")
    time.sleep(1)
    driver.find_element_by_css_selector("#lnbContent > div > div:nth-of-type(3) > ul > li > ul > li:nth-of-type(3) > a > span").click()
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    subjects3 = soup.select("#sub_content2 > div > table > tbody")
    for sub3 in subjects3:
        result=[]
        sub = sub3.select('tr')
        val += str(sub) + "<br/>"
        print(sub)
        result.append(val)
        results.append(result)
    time.sleep(1)
    driver.back()
    time.sleep(1)
    driver.back()
    time.sleep(1)
    if(i==len(subjects)-1):
        break


time.sleep(1)


file = open('html_test.html', 'w', encoding='UTF-8')

file.write(val)
file.close()
driver.back()
driver.close()
