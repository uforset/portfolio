from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time, datetime
import re
import cx_Oracle
import os
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import schedule
import numpy as np
def kor_font():
    # 한글폰트 설정 변경해 봄
    mpl.rc('font', family='NanumGothic')
    mpl.rc('axes', unicode_minus=False)
    # axes 에 적용되는 유니코드에 음수 부호 설정 해제

def create_conn():  # 오라클 연동시 필요한 conn 도출
    location = "C:\instantclient_21_6"
    os.environ["PATH"] = location + ";" + os.environ["PATH"]
    cx_Oracle.init_oracle_client(lib_dir="C:\instantclient_21_6")

    conn = cx_Oracle.connect("c##together/together1234@localhost:1521/xe")
    var1, var2, var3, var4 = crawling()

    return conn, var1, var2, var3, var4

def crawling(): # 크롬 드라이버 open 후 코로나 정보 사이트의 크롤링 데이터 리스트에 담기
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
        driver = wd.Chrome(chromedriver_path)
    else:
        driver = wd.Chrome(executable_path='chromedriver.exe')

    # 웹사이트 열기
    driver.get('https://coronaboard.kr/')
    time.sleep(5)

    # 창 더보기 모두 내리기
    for idx in range(3):
        time.sleep(5)
        driver.find_element(By.ID, 'show-more').click()

    cou_name_list = []                  # 국가명
    all_confirmed_cases_name_list = []  # 확진자
    dead_person_list = []               # 사망자
    rate_list = []                      # 치명률

    time.sleep(5)
    looplen = driver.find_elements(By.CSS_SELECTOR, 'table.google-visualization-table-table>tbody>tr')
    fin_fina_buff=''    # 초기화
    fin_find_buff=''    # 초기화
    for idx in looplen:
        cou_name = idx.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').get_attribute('textContent')
        all_confirmed_cases_name = idx.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').get_attribute('textContent')
        dead_person = idx.find_element(By.CSS_SELECTOR, 'td:nth-child(4)').get_attribute('textContent')
        rate = idx.find_element(By.CSS_SELECTOR, 'td:nth-child(6)').get_attribute('textContent')

        # '한글'만 추출 ) 국가명 데이터 형태가 현재 '한국kor' 이므로 '한국' 데이터만 추출하기 위한 영역
        p = "[^가-힣]"
        hangul = re.compile(p)
        cou_name_kor = hangul.sub('', cou_name)

        if (cou_name_kor == '경기'):
            # 현재 class 명이 같아서 한국 내부의 지역 정보도 같이 리스트에 넣는 관계로,
            # 첫번째 한국 지역 데이터 '경기'가 나오면 반복문 종료
            break

        # 데이터가 'N/A' 거나 '-' 값으로 들어오면 모두 None 으로 처리 진행
        if (all_confirmed_cases_name == 'N/A' or all_confirmed_cases_name == '-'):
            all_confirmed_cases_name = 0

        if (dead_person == 'N/A' or dead_person == '-'):
            dead_person = 0

        if (rate == 'N/A' or rate == '-'):
            rate = 0

        try:
            # ',' 빼고 추출 ) 현재 확진자수, 사망자수 데이터 형태가 현재 '123,456,789(+123,456)' 이므로 '123456789(+123456)' 데이터만 추출하기 위한 영역
            if (all_confirmed_cases_name == 0):
                fin_buff1 = 0
            else:
                fin_buff1 = all_confirmed_cases_name.replace(",", "")

            if (dead_person == 0):
                fin_buff2 = 0
            else:
                fin_buff2 = dead_person.replace(",", "")

            # '(' 이후 데이터 삭제하고 추출 : 현재 확진자수, 사망자수 데이터 형태가 현재 '123456789(+123456))' 이므로 '123456789' 데이터만 추출하기 위한 영역
            if (fin_buff1 == 0):
                del_fin_buff1 = fin_buff1
                fin_fina_buff = del_fin_buff1
            else:
                idx1 = fin_buff1.find("(")
                if (idx1 == -1):
                    idx1 = len(fin_buff1)

                del_fin_buff1 = fin_buff1[:idx1]
                fin_fina_buff = del_fin_buff1.lstrip("(")

            if (fin_buff2 == 0):
                del_fin_buff2 = fin_buff2
                fin_find_buff = del_fin_buff2
            else:
                idx2 = fin_buff2.find("(")
                if (idx2 == -1):
                    idx2 = len(fin_buff2)
                del_fin_buff2 = fin_buff2[:idx2]
                fin_find_buff = del_fin_buff2.lstrip("(")

            # 정수형으로 변환 = 확진자수, 사망자수 & 실수형으로 변환 = 치명률
            fin_fina_buff = int(fin_fina_buff)
            fin_find_buff = int(fin_find_buff)
            rate = float(rate)

            print('국가명 : {}, 확진자수 : {}, {}, 사망자수:{}, {}, 치명률 : {}, {}'.format(cou_name_kor, fin_fina_buff,
                                                                              type(fin_fina_buff), fin_find_buff,
                                                                              type(fin_find_buff), rate,
                                                                              type(rate)))

        except Exception as msg:
            print(cou_name_kor, '', msg)
            continue

        finally:
            cou_name_list.append(cou_name_kor)
            all_confirmed_cases_name_list.append(fin_fina_buff)
            dead_person_list.append(fin_find_buff)
            rate_list.append(rate)

    return cou_name_list, all_confirmed_cases_name_list, dead_person_list, rate_list

def save_crawling(conn, cou_name, all_confirmed_cases_name, dead_person, rate): # 크롤링 데이터 오라클에 저장하기
    kor_font()
    cursor = ''     # 초기화
    for i in range(len(cou_name)):
        cou_name1 = cou_name[i]
        all_confirmed_cases_name1 = all_confirmed_cases_name[i]
        dead_person1 = dead_person[i]
        rate1 = rate[i]

        cursor = conn.cursor()

        value = (cou_name1, all_confirmed_cases_name1, dead_person1, rate1)
        query = "insert into CRAWLING_CORONA_INFO values (seq_cid.nextval, :1, :2, :3, :4)"
        cursor.execute(query, value)

    conn.commit()
    cursor.close()

    # 1 시각화
    kor_font()
    plt.title("1. 시각화 테스트")
    plt.plot(cou_name1, rate1, c='y', lw=1, ls="--", marker="o", ms=2, mec='r', mew=2, mfc='r')
    plt.ylim(-1, 30)

    now = str(datetime.datetime.now().date())
    plt.savefig('C:\\project\\together\\static\\image\\crawling\\corona\\' + now + '.png')

    print('save fin')

def update_crawling(conn, country_name, all_confirmed_cases, dead_person, fatality_rate):   # 크롤링 데이터 오라클에 업데이트 하기
    cursor = ''     # 초기화
    print('update execute')
    sales1 = []
    sales2 = []
    for idx in range(len(country_name)):
        print(idx)
        value = (all_confirmed_cases[idx], dead_person[idx], fatality_rate[idx], country_name[idx])
        query = "update CRAWLING_CORONA_INFO set \
                all_confirmed_cases = :1, dead_person = :2, fatality_rate = :3 where country_name = : 4"

        cursor = conn.cursor()
        cursor.execute(query, value)
        conn.commit()

    cursor.close()

    # 1 시각화
    kor_font()
    plt.rc('font', size=10)  # 기본 폰트 크기
    plt.rc('axes', labelsize=10)  # x,y축 label 폰트 크기
    plt.rc('xtick', labelsize=10)  # x축 눈금 폰트 크기
    plt.rc('ytick', labelsize=10)  # y축 눈금 폰트 크기
    plt.rc('legend', fontsize=10)  # 범례 폰트 크기
    plt.rc('figure', titlesize=10)  # figure title 폰트 크기
    plt.title("국가별 시각화")
    plt.plot([country_name[0], country_name[1], country_name[2], country_name[3], country_name[4], country_name[5],
              country_name[6], country_name[7], country_name[8], country_name[9], country_name[10], country_name[11], ],
             [fatality_rate[0], fatality_rate[1], fatality_rate[2], fatality_rate[3], fatality_rate[4],
              fatality_rate[5], fatality_rate[6], fatality_rate[7], fatality_rate[8], fatality_rate[9],
              fatality_rate[10], fatality_rate[11], ], c='y', lw=1, ls="--", marker="o", ms=2, mec='r', mew=2, mfc='r')
    plt.ylim(-1, 30)

    now = str(datetime.datetime.now().date())
    plt.savefig('C:\\project\\together\\static\\image\\crawling\\corona\\' + now + '.png')

    print('update fin')

def close_browser(conn):    # 브라우저 close
    try:
        if conn:
            conn.close()
    except Exception as msg:
        print('oracle disconnection error :', msg)

# -----------------------------------------------------------------------------------------------------------------
def job():
    conn, var1, var2, var3, var4 = create_conn()
    # crawling -> save_crawling
    # save_crawling(conn, var1, var2, var3, var4)
    update_crawling(conn, var1, var2, var3, var4)
    close_browser(conn)


if __name__ == '__main__':
    schedule.every().day.at('09:00').do(job)


