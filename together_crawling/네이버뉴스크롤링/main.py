from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time, datetime
import cx_Oracle
import sys, os

from konlpy.tag import Komoran
#시각화 이미지 처리
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import schedule
#뉴스 크롤링
class naver_crawling:
    def __init__(self):
        self.title = []
        self.url = []
        self.__page_number = 1

    def open_browser(self):
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            chromedriver_path = os.path.join(sys._MEIPASS, 'C:\chromedriver.exe')
            self.driver = wd.Chrome(chromedriver_path)
        else:
            self.driver = wd.Chrome(executable_path='C:\chromedriver.exe')
        main_url = 'https://news.naver.com/'
        self.driver.get(main_url)
        self.driver.find_element(By.CSS_SELECTOR, "ul.Nlnb_menu_list>li:nth-child(7)>a").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "div.cluster_more>a").click()
        time.sleep(2)
        self.head_crawling()
        self.crawling()

    def move_browser(self, page_number):
        txt = 'div#paging>a:nth-child(' + str(page_number) + ')'
        self.driver.find_element(By.CSS_SELECTOR, txt).click()
        time.sleep(1)
        self.crawling()

    def head_crawling(self):
        head_news = self.driver.find_elements(By.CSS_SELECTOR, "div._persist>div.cluster>div>div.cluster_body")
        for news1 in head_news:
            news_list = news1.find_elements(By.CSS_SELECTOR, 'ul>li')
            for news in news_list:
                title = news.find_element(By.CSS_SELECTOR, 'div.cluster_text>a').text
                url = news.find_element(By.CSS_SELECTOR, 'div.cluster_text>a').get_attribute('href')
                self.title.append(title)
                self.url.append(url)

    def crawling(self):
        section_body_news = self.driver.find_elements(By.CSS_SELECTOR, 'div#section_body>ul')
        for news1 in section_body_news:
            news_list = news1.find_elements(By.CSS_SELECTOR, 'li')
            for news in news_list:
                title = news.find_element(By.CSS_SELECTOR, 'dl>dt:nth-child(2)>a').text
                url = news.find_element(By.CSS_SELECTOR, 'dl>dt:nth-child(2)>a').get_attribute('href')
                self.title.append(title)
                self.url.append(url)
        if self.__page_number != 5:
            self.__page_number += 1
            self.move_browser(self.__page_number)
        else:
            self.driver.close()

    def get_title(self):
        return self.title

    def get_url(self):
        return self.url

#conn 생성
def create_conn():
    cx_Oracle.init_oracle_client(lib_dir="C:/instantclient_21_6")
    conn = cx_Oracle.connect("c##together/together1234@localhost:1521/xe")
    conn.autocommit = False
    return conn

#conn 닫기
def close_cone(conn):
    conn.close()

#커밋
def commit_conn(conn):
    conn.commit()


# 뉴스테이블 입력값
def save_oracle_crawling(conn, tit, url):
    tp_value = ()
    cursor = ''
    for i in range(len(tit)):
        tp_value = (tit[i], url[i])
        query = "insert into CRAWLING_NAVER_NEWS values (seq_id.nextval, :1,:2)"
        try:
            cursor = conn.cursor()
            cursor.execute(query, tp_value)  # execute할때 튜플을 넣어 쿼리문에 적용시킴
            #commit_conn(conn)
        except:
            #conn.rollback()
            cursor.close()
            continue
        finally:
            continue

#뉴스 키워드 카운터 db로 저장
def save_oracle_country_count(conn, tp_value):
    cursor = ''
    for i in range(len(tp_value)):
        query = "update CRAWLING_COUNTRY set keyword_count= :1 where country_name = :2"
        try:
            cursor = conn.cursor()
            print(tp_value[i])
            cursor.execute(query, tp_value[i])  # execute할때 튜플을 넣어 쿼리문에 적용시킴
            commit_conn(conn)
        except:
            conn.rollback()
            cursor.close()
            return
        finally:
            continue

#현재 키워드 카운터 호출
def open_oracle_country_count(conn):
    cursor = ''
    query = "select country_name,keyword_count from CRAWLING_COUNTRY"
    try:
        cursor = conn.cursor()
        cursor.execute(query)  # execute할때 튜플을 넣어 쿼리문에 적용시킴
        result = cursor.fetchall()
        return dict(result)
    except Exception as msg:
        print(msg)
        cursor.close()

#분석     튜플형식의 뉴스정보, 국가정보
def Noun_count(title, c_name):
    komoran = Komoran()
    for line in title:
        malist = komoran.pos(''.join(line))
        # 명사들을 수집해서 반복되는 명사 count 를 진행한다.
        for word in malist:
            if word[1] == 'NNP':
                if not (word[0] in c_name):
                    continue
                c_name[word[0]] += 1
    keys = list(zip(c_name.values(), c_name.keys()))
    full = {}
    for k,v in c_name.items():
        if v!=0:
            full[k]=v

    showwordcloud(full)
    return keys

def showwordcloud(c_name):
    wordcloud = WordCloud(font_path='C:/windows/fonts/malgun.ttf', background_color='white', width=600, height=400,
                          max_font_size=100).generate_from_frequencies(c_name)
    now = datetime.datetime.now().date()
    file_link = 'C:\\project\\together\\static\\image\\crawling\\naver\\' + str(now) + '.png'
    wordcloud.to_file(filename=file_link)
    plt.figure(figsize=(10, 10))
    plt.imshow(wordcloud)
    plt.axis("off")

def job():
    try:
        os.chdir(sys._MEIPASS)
        print(sys._MEIPASS)
    except:
        os.chdir(os.getcwd())
    crawling = naver_crawling()
    crawling.open_browser()
    conn = create_conn()
    save_oracle_crawling(conn, crawling.get_title(), crawling.get_url())
    t = Noun_count(crawling.get_title(), open_oracle_country_count(conn))
    save_oracle_country_count(conn, t)
    close_cone(conn)
    print('종료!')

if __name__ == '__main__':
    schedule.every().day.at('09:00').do(job)
    