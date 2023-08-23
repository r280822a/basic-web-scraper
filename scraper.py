from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Open YouTube channel
username = ""
url = "https://www.youtube.com/@"+username+"/videos"
browser = webdriver.Chrome()
browser.get(url)

# Reject all additional cookies, Play latest video
browser.find_element("xpath","/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[1]/div/div/button").click()
browser.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[1]/div/ytd-rich-item-renderer[1]/div/ytd-rich-grid-media/div[1]/div[1]/ytd-thumbnail/a").click()

# Quit script after input
running = True
while(running):
	inp = input()
	if inp != "":
		quit = False