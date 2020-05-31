import requests
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def randomSong():
    print("This program is for selecting a random song by an artist of your choosing")
    while True:
        artist = input("Enter an artist's name: ")
        if artist != 'exit':
            url = 'https://api.deezer.com/search?q=artist:"' + artist + '"'
            r = requests.get(url)
            rand_number = random.randint(0,25)
            song =  r.json()["data"][rand_number]["title"]
            album = r.json()["data"][rand_number]["album"]["title"]
            print('\n' + "Song: " + song)
            print("Album: " + album)

            listen = input('Type yes if you would like to listen to this song or no if you don\'t want to: ')
            PATH = "C:\Program Files (x86)\chromedriver.exe"
            if listen == 'yes':
                driver = webdriver.Chrome(PATH)
                driver.maximize_window()
                wait = WebDriverWait(driver, 4)
                driver.get("https://www.youtube.com/results?search_query=" + song + ' ' + artist) # opens youtube and searches for song
                #driver.get("https://music.youtube.com/search?q=" + song + ' ' + artist)
                #wait.until(EC.presence_of_element_located((By.ID, 'content')))
                #driver.find_element_by_id('content').click()
                
                driver.find_element_by_id('thumbnail').click()  # clicks on first video thumbnail

            print("Type 'exit' to end the program\n")
        else:
            break

randomSong()