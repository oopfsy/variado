#coding: utf-8
#title_en: Pornpics
#https://www.pornpics.com/
import downloader
from utils import Downloader, clean_title


@Downloader.register
class Downloader_pornpics(Downloader):
    type = 'pornpics'
    URLS = ['.pornpics.com']
    icon = 'base64:AAABAAEAICAAAAEAIAAoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP/+/w3///9o/v7+zvz8/P7////////////+///////////////////////////////////+/v////7///////////////////7////////////////+//////////////z8/P7+/v/O////cP///w0AAAAAAAAAAAAAAAD///8s/f38qP7+/vT+///////////////+//////////7//////////////////////////v/////+///+///////////////////////////////+///////////////////////////////8/Pz+/v7+sv7+/iwAAAAA////Dfz9/aj///////7//////////////////////////////////////////v////////////////////////////////////////////////////7//////////////v/////////////////////+/////v////7+sv7//w3///5e/v7+9P///////////////////v////////7////////+///////+//////////7//////////////////////////////////////////////////////////////////////////////v/////+///////8/Pz+////cP///8D///////////////////////////7//////////////////////v////////////////////////////////////////////////////////////////////////7///////7///////////////////7//////////v7O/v7+9P/////////////////+/////////v////////////////////////////////////////////////////////////////////br/v/dsvr/zpT2/+7b+v////7////////////////////////////////////+//z8/P7//////////////////////////////v///v/////////+///+/////////////////////////////////////////+7b+v/OlPb/tFj0/6U18v+gK/H/vGz1//r0//////////7////////////////////+//////////////////////////7///////////////7///z8/P69vb3/mJiY/5iYmP+YmJj/mJiY/5iZmf+YmJj/mZiY/5iYmP+YmJj/kIaZ/4x8l/+MfZb/jXyW/4x8lv+MfJb/wsHC//z8/P7////////////////////////////+///+//////////////////7//v//////////////wsHC/xMTEv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wEAAP8AAAD/AAAA/wABAP8AAAD/AAAA/wAAAP8jIiP/0M/Q/////////////v////////////////7////////////////+//////////////////////+enp7/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAEA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wUEBP+xsbH/////////////////////////////////////////////////////////////////7tv6/5iYmP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAf8AAQD/AAAA/wAAAf8AAAH/AAEA/wAAAP8AAAD/AAAA/wEAAf8AAAD/BQUF/7Gxsf///////v/////////+/////////////////v///////////////////v///+7b+v+sRvP/kYaZ/xMTEv9JSkn/SUpI/0lLSf9JSkn/SUpI/0lKSf9ISkn/SUpJ/0lKSf9JSkn/SUpJ/0lKSf9JSkj/SEtJ/0lKSf8TExL/sbGx/////v/////////////////////////+////////////////////////////58r7/6Q18v+MfJb/YWFh//z8/P78/Pz+/Pz9/vz8/P79/P3+/Pz8/vz8/P78/Pz+/Pz8/vz8/P78/Pz+/Pz8/vz8/P78/fz+8vLy/zo7Ov+srK3////////+//////7///////////////////////7//v/////////////////36/7/tFj0/4x8lv9oaGj///////r0///OlPb/7tv6///////myvv/3bL6/+fK+/+9bPT/x4H3/92y+/+9bPX/3bL6///////z8/L/SUpJ/6GQrP/nyvv//////////////////////////v/////////////////////////+//7//v/To/T/jXyW/2hoaf//////9uv//6U18v/nyvv//////86U9v+0WPT/tFj0/7xs9f/Ggff/zpT2/71s9f+sRvP/+vT///Ly8v9JSkn/nYer/8eB9//8/Pz+//////////////////////7///////////////////////////////br/v+Rhpn/aGho///////26/7/oCvx/71s9f/ny/v/zpT2/6xG8/+sRvP/7tv6//r0///dsvr/rEbz/86U9v///v//8vLy/0lKSf+fiq3/rEbz/+7b+v/////////+///////////////+//////////////////7+/////////////5iYmP9oaWn///////br/v+gK/H/pTTy/6Ar8f+0WPT/vW31/7xt9P+sRvP/tFj0/71s9f+gK/H/06P0///////y8vP/SEpJ/56KrP+gK/H/06P1/////////v/////+///////////////+////////////////////////////mJiY/2loaP//////9uv+/6U18v/dsvr/rEbz/71s9f/nyvv/+vT//92y+v/nyvv/9uv+/92y+v/u2/r///////Ly8v9JSkn/q6Gy/6U18v+0WPT//Pz8/v////////////////////////////////////////////////////+YmJj/aGho///////26/7/pTXy/6Ar8P+gK/H/vWz1/8eB9v////7//////////////v//////////////////8vLy/0lKSf+xsbH/x4H3/5UT7v/u2/r//////////v///////////////////v///v///////v///////////5iYmP9oaGj///////38/P7dsvv/zpT2/+fL+v/u2/r/58r7/////////////////////////////v/////////y8vL/SUpJ/6ysrP/To/T/lRLu/92y+v/////////////////////////+////////////////////////////mJiY/2hoaP////////////////////7///////////////////////////////////////////////7///////Ly8v9JSkn/oZCs/6Er8f+gK/H/58r6///////////////////////////////////////////////////+//+enp7/Ojs6/6ysrP+srKz/rK2s/6ysrP+sraz/rKys/6ysrP+srKz/rKys/6ysrP+srKz/rKys/6ysrP+srKz/np6e/yMjI/+robP/zpT2/+fL+//////////////////////////+///+/////////////////////////Pz8/vLy8v9hYWH/Ojs6/zo7Ov86Ozr/Ozs6/zo7Ov86Ozr/Ojs6/zo7Ov86Ozr/Ojs6/zo6Ov86Ozr/Ojs6/zo7Ov86Ozr/aGlo//Ly8v////////////////////////////////////////////////////////7///////////////7///z8/P7u2/r/06P0/+7a+v/y8vL/8vLy/+fK+//To/T/zpX3/86U9v/To/T/79v7//Lz8v/y8vL/8vLy//Ly8v/8/Pz+/v/+//////////////////////////////////////////7///////////////////////7//////////////+7b+v+VE+7/x4H3/86U9v+sRvP/lRPu/5UT7v+sRvP/x4H3/+fL+//69P7////////+///////////////+/v////////////////////7//////////////v7//////////////////////////////////v/////+/////////Pz9/r1t9f+VE+//lRPu/6U18v/Hgfb/58r7//r0/////////////////////////////////////////////////////v///////////////////////////v///////v7/9P///v/////////////////////////////+////////9uv+/92y+v/ny/v/+vT////+/v////////////////////////////////////////////////////////////////////////////////////////////7+/vT////A///////////////////////////////////////////+///////////////+/v///////////////v///v////7//////////////////v////////////////////////7//////v///////////////v///////v7+zv///l7///70///+//7+//////7//////////v/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////+//7+/vT+//9o/v//Df39/Z////////////7////////////+/////v///v7//////////////////////////////////////////////////v/+/////v///////////////v///////////////////////////////////////f39qP///w0AAQAA////LP39/J/+/v70//////////////////////////////7//////////v////////////////////////////7+///+//////////////////////////////////7//////////////////v7+9P39/Kj///4sAQAAAAAAAAAAAAAA////Df///17////A/v7+9P///////////v/////////////////////+//////////////7////+/////v////////////////7////////////////////+//////7//v7+9P///8D///9e////DQAAAAAAAAAA'
    display_name = 'Pornpics'
    MAX_CORE = 3
    ACCEPT_COOKIES = [r'(.*\.)?(pornpics\.com)']

    def read(self):
        self.urls, self.filenames, self.title = get_imgs_www(self.url)

def get_imgs_www(url):
    soup = downloader.read_soup(url)
    title = soup.find('h1').text.strip()
    channel = soup.find('div', class_='gallery-info__item').find('a').text.strip()
    models = soup.find('div', class_='gallery-info__content').findAll('a')
    nmodels = []
    num = 0
    for a in models:
        num += 1
        nmodels.append(a.text.strip())
        if num == 3:
            break 
    views = soup.find('div', class_='gallery-ps4').findAll('a')
    imgs = []
    for a in views:
        imgs.append(a.attrs['href'])
    filenames = {}
    num = -1
    for img in imgs:
        num += 1
        filenames[img]=str(num) + '.jpg'
    title =  clean_title(channel+ ')' + title +'('+ ",".join(nmodels))
    return imgs, filenames, title