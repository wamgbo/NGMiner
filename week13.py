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
        time.sleep(1)
        source=driver.page_source
        self.soup=BeautifulSoup(source,'html.parser')
        driver.quit()
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
        except KeyboardInterrupt as e:
            exit()
            print(e)
    def _print_version(self):
        count=0
        for i,j in enumerate(self._inital_db()):
            print("version:",j,"(",count,")")
            count+=1
    def _inital_db(self):
        driver_dict = {
            "591.44": '258949',
            "581.80": '257597',
            "581.57": '257398',
            "581.42": '257266',
            "581.29": '254559',
            "581.15": '253200'
        }
        return driver_dict
    def info(self):
        web=self.soup
        for i in web.find_all("a"):
            i.decompose()
        title=web.find_all("span",class_="RsltDtlsHeadingCell")
        content=web.find_all("span",class_="RsltDtlsValueCell")
        print('='*40)
        for i in range(0, 5):
            print(title[i].contents[0], end='')
            html_block = str(content[i])
            clean = BeautifulSoup(html_block, "html.parser").get_text(separator="")
            clean = clean.strip()
            print(clean)
        print('='*40)
        release_notes=web.find("h2",id="lclReleaseNotes")
        release_notes_div=web.find("div",id="ddReleaseNotes_div")
        html = "".join(str(x) for x in release_notes_div.contents)#把 <div> 內的所有內容整合成一個 HTML 字串。
        clean_notes = BeautifulSoup(html, "html.parser").get_text(separator="\n").strip()#將剛剛合併的 HTML 字串解析成 BeautifulSoup 物件。 separator="\n" 代表每個區塊之間用換行符號分開（避免文字黏在一起）。去掉字串開頭和結尾的多餘空白或換行。        
        lines = [line.strip() for line in clean_notes.splitlines() if line.strip()]#clean_notes.splitlines()將文字按換行符號分割成列表，每一行變成一個元素。
        print(release_notes.contents)
        for i in lines:
            print(i)
            print()
        print('='*40)
craw=webcraw()
craw.info()
