from googleapiclient.discovery import build
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

api_key = 'your You Tube Api key'

def get_videos_search(keyword):
    youtube = build('youtube', 'v3', developerKey=api_key)
    youtube_query = youtube.search().list(q=keyword, part='id,snippet', maxResults=5)
    youtube_res = youtube_query.execute()
    return youtube_res.get('items', [])
x = ['鈴木亜美','フォルダー５','パフューム','KARA mr','安室奈美恵']
result = get_videos_search(random.choice(x))
for item in result:
    if item['id']['kind'] == 'youtube#video':
        print(item['snippet']['title'])
        print('https://www.youtube.com/watch?v=' + item['id']['videoId'])

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

# Navigate to url with video being appended to search_query
driver.get('https://www.youtube.com/watch?v=' + item['id']['videoId'])

# play the video
wait.until(visible((By.ID, "video-title")))
driver.find_element_by_id("video-title").click()
 