import time
import random
import requests
from bs4 import BeautifulSoup
from pytictoc import TicToc

class curry:
    # The best ever shooter in the NBA
    def __init__(self):
        pass

    def printname(self):
        print("I am stephen curry")

    def accuracy(self) -> float:
        # Scrapes basketballreference to retrieve curry's 3PFG%
        url = 'https://www.basketball-reference.com/players/c/curryst01.html'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        info = soup.find(id="info")
        stats_pullout = info.find_all(class_="p2")[0]
        ptags = stats_pullout.find_all('p')
        accuracy = float(ptags[3].get_text())
        return accuracy


if __name__ == "__main__":

    # setup
    t = TicToc()
    stephen30curry = curry()
    #t.tic()
    chance = stephen30curry.accuracy()
    #t.toc()
    
    # intro
    print("Welcome to curry-shot!")
    time.sleep(1)
    print(f"Shooting accuracy is {chance}")
    time.sleep(1)
    print("Shooting your shot!")
    shoot = random.uniform(0, 100)
    time.sleep(1)
    # Result!
    if chance <= shoot: 
        print("CURRRYY!!") 
    else: 
        print("Next time brah")




