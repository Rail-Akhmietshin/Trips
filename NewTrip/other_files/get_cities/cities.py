from selenium import webdriver
from bs4 import BeautifulSoup
from NewTrip.settings import BASE_DIR
import os

# total_result = []

# driver = webdriver.Edge()

# page = 1

# while page < 89:
#     new_url = f'https://tochka-na-karte.ru/modules/travel/territories_data.php?page={page}&type=9999&id=63'
#     driver.get(new_url)

#     soup = BeautifulSoup(driver.page_source, 'lxml')

#     name = soup.find_all("a", class_="lnk05")
#     category = soup.find_all("span", class_="sign3")

#     match = zip([x.text for x in name], [y.text for y in category])

#     total_result += list(map("".join, match))
    
#     page += 1
    

# driver.close()

# with open("./cities.txt", "w", encoding="utf-8") as file:
#     file.write("\n".join(total_result))



path = os.path.join(BASE_DIR, "other_files/get_cities/cities.txt")

with open(path, "r", encoding="utf-8") as file:
    cities = file.read().split("\n")

for i, x in enumerate(cities):
    templates = [", город", ", пгт"]
    for template in templates:
        if template in x:
            cities[i] = cities[i].replace(template, "")








