import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
class webcraw:
    def __init__(self):
        url='https://www.nvidia.com/zh-tw/geforce/drivers/results/'
        self._print_version()
        version=self.select_version()
        self.url=url+version+'/'
        driver = webdriver.Chrome()
        driver.get(self.url)

        source=driver.page_source
        self.soup=BeautifulSoup(source,'html.parser')
    def select_version(self):
        return self._select_version()
    def _select_version(self):
        try:
            version=int(input("請選擇版號(.e.g.591.44 input:0):"))
            db=self._inital_db()
            driver_list=list(db)
            return db[driver_list[version]]
        except Exception as e :
            print(e)
            
    def _print_version(self):
        count=0
        for i,j in enumerate(self._inital_db()):
            print("version:",j,"(",count,")")
            count+=1
    def _inital_db(self):
        driver_dict = {
            "591.44": '258949',
            "581.80": '257597'
        }
        return driver_dict
        
    def result(self):
        print(self.soup)
    
    def info(self):
        web=self.soup
        title=span = web.select_one('#ddVersionLbl_td span')
        print(title)
        



craw=webcraw()
craw.info()
