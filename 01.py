# coding: SJIS
import requests
import bs4
print("ScriptStart")
res = []
res.append(requests.get('https://kinezo.jp/pc/schedule?ush=140feb4'))
cnt = 1
for resp in res:
	resp.encoding = resp.apparent_encoding
	print(resp.status_code)
	resp.raise_for_status()
	soup = bs4.BeautifulSoup(resp.text, "html.parser")
	titles = soup.select('.cinemaTitle.elp')
	print("----title----")
	print(titles[0].text)
	print("----title2----")
	print(titles[1].text)
	stTimes = soup.select('div[class*="scType"]')
	print("----time1----")
	print(stTimes[0].text)
	print("----time2----")
	print(stTimes[1].text)
	print(cnt)
	cnt+=1
