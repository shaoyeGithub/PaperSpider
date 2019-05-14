import requests
from selenium import webdriver
import time
import  math
import xlwt,xlrd
from xlutils.copy import copy

def work():
    browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    url = 'https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=((%22machine%20learn*%22%20OR%20%22deep%20learning%22%20OR%20%22neural%20network%3F%22%20OR%20%22reinforcement%20learning%22%20OR%20%22unsupervised%20learn*%22%20OR%20%22supervised%20learn*%22)%20AND%20(%22software%20engineering%22%20OR%20defect%20OR%20%22software%20requirement%3F%22%20OR%20%22software%20design%22%20OR%20%22software%20test*%22%20OR%20%22software%20maintenance%22%20OR%20%22source%20code%22%20OR%20%22project%20management%22%20OR%20%22software%20develop*%22))&highlight=true&returnType=SEARCH&ranges=2009_2018_Year&returnFacets=ALL&refinements=ContentType:Conferences&refinements=ContentType:Journals%20.AND.%20Magazines'

    browser.get(url)
    time.sleep(5)

    # firstStep = browser.find_element_by_xpath('//*[@id="xplMainContent"]/div[1]/div[1]/ul/li[2]/xpl-select-dropdown/button/a')
    # firstStep.click()
    #
    # time.sleep(3)
    # perpage = browser.find_element_by_class_name('filter-popover-content')
    # perpage.find_element_by_xpath('./li[5]').click()
    # perpage.click()

    # 总共的论文数量
    # AllPaper = browser.find_element_by_xpath('//*[@id="xplMainContent"]/div[1]/div[2]/xpl-search-dashboard/section/div/div[1]/span[1]/span[2]')
    # AllPaper = AllPaper.text.replace(',','')
    # AllPaper = int(AllPaper)
    # print(AllPaper)

    # 4645 是论文数量
    try:
        for i in range(0,math.ceil(4645/25)):
        # for i in range(0,2):
            print("第"+ str(i) + '页')
            # time.sleep(10)
            btn = browser.find_element_by_class_name('loadMore-btn')
            browser.execute_script("arguments[0].scrollIntoView()", btn)
            btn.click()
    except:
        papers = browser.find_elements_by_xpath('//*[@class = "col result-item-align"]')


        getsum = 0
        par = 0
        print()
        wb = xlwt.Workbook()
        ws = wb.add_sheet('A Test Sheet')
        for paper in papers:
            par += 1
            print('-----------------------------------------')
            print('第:'+ str(par) +' 个 paper')
            name = paper.find_element_by_xpath('./h2/a')
            print("paper title:"+ name.text)

            third = paper.find_element_by_xpath('./div[1]/a')
            print(third.text)

            startpage = paper.find_element_by_xpath('./div[1]/div[2]/span/span[2]')
            endpage = paper.find_element_by_xpath('./div[1]/div[2]/span/span[4]')

            print(startpage.text, end=" ")
            print(endpage.text)

            year = paper.find_element_by_xpath('./div[1]/div[1]/span[1]')
            print(year.text)

            if 'workshop' in third.text or 'companion' in third.text:
                continue
            if '-' in startpage.text:
                startIndex = startpage.text.index('-')
                startIndex = startIndex + 1

                endIndex = endpage.text.index('-')
                endIndex = endIndex + 1

                paperNum = int(endpage.text[startIndex:]) - int(startpage.text[endIndex:]) + 1
            else:
                paperNum = int(endpage.text) - int(startpage.text)
            if paperNum < 8:
                continue

            getsum += 1
            ws.write(getsum, 0, name.text)
            ws.write(getsum, 1, year.text[5:])

        wb.save(r'C:\Users\FEITENG\Desktop\IEEE.xls')

    # print("title")
    # names = browser.find_elements_by_xpath('//*[@class = "col result-item-align"]/h2/a')
    # for name in names:
    #     print(name.text)

    #第三行描述
    # third = browser.find_elements_by_xpath('//*[@class = "description"]/a')
    # for str in third:
    #     print(str.text)

    #页数
    # print("page")
    # # page = browser.find_elements_by_xpath('//*[@class = "description"]/div[2]/span')
    # startpages = browser.find_elements_by_xpath('//*[@class = "description"]/div[2]/span/span[2]')
    # endpages = browser.find_elements_by_xpath('//*[@class = "description"]/div[2]/span/span[4]')

    # for i in pages:
    #     startPage = i.find_element_by_xpath('//span[2]').text
    #     endPage = i.find_element_by_xpath('//span[4]').text
    #
    #     print(startPage,end=" ")
    #     print(endPage)
        # pageNum = int(endPage) - int(startPage)
        # print(pageNum)

    # for i in range(len(startpages)):
    #     if startpages[i].text != '' and endpages[i].text != '':
    #         start = int(startpages[i].text)
    #         end = int(endpages[i].text)
    #         print(start,end=" ")
    #         print(end)
    #
    #         page = end - start + 1
    #         print(page)
    # start = list()
    # end = list()
    # for page in startpages:
    #     if page.text != '':
    #         if page.text[:3] == 'V3-':
    #             start.append(int(page.text[3:]))
    #         else:
    #             start.append(int(page.text))
    # for page in endpages:
    #     if page.text != '':
    #         if page.text[:3] == 'V3-':
    #             end.append(int(page.text[3:]))
    #         else:
    #             end.append(int(page.text))
    #
    # print(start)
    # print(end)
    # #年份
    # years = browser.find_elements_by_xpath('//*[@class = "description"]/div[1]/span[1]')
    # for year in years:
    #     print(year.text)



if __name__ == '__main__':
     work()
