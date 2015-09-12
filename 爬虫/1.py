#coding:utf-8

import urllib2
import urllib
import re




def get_pagenum(Page_num,ac):
    AC = [ac,]
    for i in range(1,Page_num):
        x = ac+'_'+str(i+1)
        AC.append(x)
    return AC

def pachong(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent' : user_agent}
    req = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(req)
    return response.read()

ac = raw_input('输入ac号：')
url = 'http://www.acfun.tv/a/'+ac
print url
page = pachong(url)


page_num = re.search(r'data-total="\d"', page)
if page_num is not None:
    Page_num = re.findall(r'(\w*[0-9]+)\w*',page_num.group())
    Page_Num = int(Page_num[0])
else:
    Page_Num = 1
AC = get_pagenum(Page_Num,ac)


for i in range(Page_Num):
    url = 'http://www.acfun.tv/a/'+AC[i]
    page = pachong(url)

    #reload(sys)
    #sys.setdefaultencoding('utf-8')
    #unicodePage = page.decode("utf-8")
    txt = '<a class="btn success active" href="/a/ac2093541" title="Part \d"><i class="icon icon-play-circle"></i>(.*?)</a>'
    new_txt = re.sub(r'ac2093541',AC[i],txt)
    #print new_txt
    myItems = re.findall(new_txt,page,re.S)
    #print myItems
    zhengw =re.findall('<p style="box-sizing: border-box; margin: 5px 0px; padding: 0px; outline: 0px; border: 0px; vertical-align: baseline;"><font face="Helvetica Neue, Helvetica, Arial, STHeiti, Microsoft Yahei, sans-serif"><span style="font-size: 16px; line-height: 16px;">&nbsp; &nbsp;(.*?)</span></font></p>',page,re.S)

    f  = open('005.txt','a+')
    for i in myItems:
        f.write(i)
        f.write('\n')
        f.write('\n')
    for z in zhengw:
        f.write('   ')
        f.write(z)
        f.write('\n')
f.close()
