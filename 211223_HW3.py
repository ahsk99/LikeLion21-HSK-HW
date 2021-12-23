
import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오기
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#Google Chrome에서 단어/해당 섹션 우클릭 > INSPECT > 하이라이트된 문장 > copy > copy selector
#select를 이용해서, tr"들"을 불러오기
songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

# songs(tr들)의 반복문을 돌리기; select_one 사용해서 하나씩!!
for song in songs: 
    a_tag = song.select_one('td.info > a.title.ellipsis')
    if a_tag is not None:
        rank = song.select_one('td.number').text.split()[0]
        title = song.select_one('a.title.ellipsis').text.strip()
        singer = song.select_one('a.artist.ellipsis').text.strip()
        print (rank, title, singer)

#PYTHON
#split() returns a list of strings; can take 2 params: 'separator', 'maxsplit'.
#strip() removes leading and trailing whitespaces; can take param 'chars' to det. which characters to get rid of front and back.

# html 
# tr stands for table row.
# td stands for table data / cells.
# th stands for table header.

# # 선택자를 사용하는 방법 (copy selector)
# soup.select('태그명')
# soup.select('.클래스명')
# soup.select('#아이디명')

# soup.select('상위태그명 > 하위태그명 > 하위태그명')
# soup.select('상위태그명.클래스명 > 하위태그명.클래스명')

# # 태그와 속성값으로 찾는 방법
# soup.select('태그명[속성="값"]')

# # 한 개만 가져오고 싶은 경우
# soup.select_one('위와 동일')     