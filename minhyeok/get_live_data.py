import requests
from bs4 import BeautifulSoup

# 전국 (17 도, 광역시)

korea = requests.get('https://www.weather.go.kr/weather/observation/currentweather.jsp')
korea_soup = BeautifulSoup(korea.content,"html.parser")
korea_table = korea_soup.find('table',{'class':'table_develop3'})

korea_data = []

for tr in korea_table.find_all('tr'):
    tds = list(tr.find_all('td'))
    
    for td in tds:
        if td.find('a'):
            point = td.find('a').text
            temp = tds[5].text
            humidity = tds[9].text
            korea_data.append([point, temp, humidity])

korea_new = []
city = ['서울', '인천', '수원', '원주', '청주', 
        '대전', '세종', '천안', '순천', 
        '전주', '광주', '창원', '울산', 
        '부산', '포항', '대구', '제주']

for i in korea_data:
    if i[0] in city:
        korea_new.append(i)

# 영남
# yeongnam = requests.get('https://www.weather.go.kr/weather/observation/currentweather.jsp?auto_man=m&stn=0&type=t99&reg=159&x=22&y=5&tm=2021.05.23.20%3A00')
# yeongnam_soup = BeautifulSoup(yeongnam.content,"html.parser")
# yeongnam_table = korea_soup.find('table',{'class':'table_develop3'})

# yeongnam_data = []

# for tr in yeongnam_table.find_all('tr'):
#     tds = list(tr.find_all('td'))
    
#     for td in tds:
#         if td.find('a'):
#             point = td.find('a').text
#             temp = tds[5].text
#             humidity = tds[9].text
#             yeongnam_data.append([point, temp, humidity])


# korea_new
# yeongnam_data

# '\xa0' => NULL


 
 
