from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options();
options.add_argument("user-data-dir=C:\\Users\\dell\\AppData\\Local\\Google\\Chrome\\User Data");

web = webdriver.Chrome(executable_path='D:/Dell/Downloads/Apps/chromedriver.exe');




web.get("https://www.almuheet.net/163262/#%D9%85%D8%B0%D9%83%D8%B1%D8%A9_%D8%AF%D8%A7%D8%AE%D9%84%D9%8A%D8%A9_%D8%AC%D8%A7%D9%87%D8%B2%D8%A9https://www.almuheet.net/163262/#%D9%85%D8%B0%D9%83%D8%B1%D8%A9_%D8%AF%D8%A7%D8%AE%D9%84%D9%8A%D8%A9_%D8%AC%D8%A7%D9%87%D8%B2%D8%A9https://www.almuheet.net/163262/#%D9%85%D8%B0%D9%83%D8%B1%D8%A9_%D8%AF%D8%A7%D8%AE%D9%84%D9%8A%D8%A9_%D8%AC%D8%A7%D9%87%D8%B2%D8%A9https://www.almuheet.net/163262/#%D9%85%D8%B0%D9%83%D8%B1%D8%A9_%D8%AF%D8%A7%D8%AE%D9%84%D9%8A%D8%A9_%D8%AC%D8%A7%D9%87%D8%B2%D8%A9https://www.almuheet.net/163262/#%D9%85%D8%B0%D9%83%D8%B1%D8%A9_%D8%AF%D8%A7%D8%AE%D9%84%D9%8A%D8%A9_%D8%AC%D8%A7%D9%87%D8%B2%D8%A9https://www.almuheet.net/163262/#%D9%85%D8%B0%D9%83%D8%B1%D8%A9_%D8%AF%D8%A7%D8%AE%D9%84%D9%8A%D8%A9_%D8%AC%D8%A7%D9%87%D8%B2%D8%A9")

# for cookie in pickle.load(open("AVONcookies.pkl", "rb")): 
# web.add_cookie(cookie) 
web.find_element_by_xpath('//*[@id="article-body"]/ul').text
