from requests_html import HTMLSession
import speech_to_text
#class="degree-unit-button fz-16 bgc-none bd-0 p-0 cur-p"
def weather():
    s = HTMLSession()
    query = "Kolkata"
    url = f'https://in.search.yahoo.com/yhs/search?hspart=sz&hsimp=yhs-002&p=weather+Kolkata&type=type80160-18484002&param1=3179868600+{query}'
    r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'})
    temp = r.html.find()

weather()
