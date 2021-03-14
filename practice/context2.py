import requests
from bs4 import BeautifulSoup
import random
from multiprocessing import Pool, cpu_count

##get proxy list from https://free-proxy-list.net/
def get_ip(url, ip=None, ua=None):
    session = requests.Session()
    session.proxies = ip
    session.trust_enc = False
    print(session.get(url).text)
    #res = requests.get(url, headers=ua, proxies=ip, verify=False).text
    #soup = BeautifulSoup(res, 'lxml')
    #my_ip = soup.find('table').find('tbody').find_all('tr')#.find('span').text
    #with open('proxies.txt', 'a') as f:
     #   for i in my_ip:
     #       f.writelines(f"{i.find_all('td')[:2][0].text}:{i.find_all('td')[:2][-1].text}")
    #        f.writelines('\n')
    #print(res)
##check is valid proxy from list
def main(ip):
    url = 'https://2ip.ru/'
    useragents = []
    with open('useragents.txt', 'r') as f:
        useragents += f.read().split('\n')
    proxy = {
        'https': f'https://{ip}'
    }
    #useragent = {
    #    'User-Agent': random.choice(useragents)
    #}
    #print(proxy, useragent, sep='\n')
    try:
        print(f'{get_ip(url, proxy)}')#, useragent)}')
    except Exception:
        print(f'ip is not availible')
get_ip('https://2ip.ru/', {'https': f'https://118.27.114.32:8080'})

#if __name__ == "__main__":
#     ip_list = []
#     get_ip('https://free-proxy-list.net/')
#     with open('proxies.txt', 'r') as f:
#         ip_list += f.read().split('\n')[:-1]
#     with Pool(cpu_count()) as process:
#         process.map(main, ip_list)
     #print(ip_list)
