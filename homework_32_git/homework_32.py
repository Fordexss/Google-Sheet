from bs4 import BeautifulSoup

path_to_mY_file = "C:\\Users\\Vlad\\Desktop\\Practice\\Python\\homework_32_git\\text.html"

with open(path_to_mY_file) as file:
    soup = BeautifulSoup(file, "html.parser")

for data in soup.find(id="main-title"):
    print(f"Головний заголовок: {data.text}")

for data in soup.select(".services-list"):
    print(f"Сервіси: {data.text}")

for data in soup.select("footer > p"):
    print(f"Футер текст: {data.text}")