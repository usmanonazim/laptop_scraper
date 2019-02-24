from requests import get
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from time import time
from random import randint

# url = "https://www.currys.co.uk/gbuk/computing/laptops/laptops/315_3226_30328_xx_xx/xx-criteria.html"
# response = get(url)
# page_html = BeautifulSoup(response.text, 'html.parser')
# product_info = page_html.find_all('div', class_='desc')
# brand_name = product_info[0].find('span', attrs=({'data-product':'brand'})).text
# #print(brand_name)
# product_name = product_info[0].find('span', attrs={'data-product':'name'}).text
# #print(product_name)
# savings = product_info[0].find_all('span', class_='past-amount')
# #print(savings[0].text.lstrip().rstrip())
# current_price = product_info[0].find(class_='price').text
# current_price = current_price.lstrip().rstrip()
# #print(current_price)

brands = []
prices = []
infos = []
page_url = [str(i) for i in range(2,20)]
start_time = time()
requests = 0
for page in page_url:
    response = get(
        "https://www.currys.co.uk/gbuk/computing/laptops/laptops/315_3226_30328_xx_xx/" + page + "_20/relevance-desc/xx-criteria.html")
    sleep(randint(6, 8))

    print(response.status_code)

    requests += 1

    elapsed_time = time() - start_time

    print('Request:{}; Frequency: {} requests/s'.format(requests, requests / elapsed_time))

    page_html = BeautifulSoup(response.text, 'html.parser')

    product_info = page_html.find_all('div', class_='desc')

    for prod in product_info:
        #brand of each laptop
        brand = prod.find('span', attrs=({'data-product': 'brand'})).text
        brands.append(brand)
        #price of each laptop
        price = prod.find(class_='price').text
        price = price.lstrip().rstrip()
        prices.append(price)
        #description
        info = prod.find('span', attrs={'data-product': 'name'}).text
        infos.append(info)

laptop_data = pd.DataFrame({'Brand': brands,
                            'Info':infos,
                            'Price':prices})
laptop_data.to_csv('laptop_data.csv', index=False, encoding='utf-8')
print(laptop_data)


