import gspread
import pandas as pd
from matplotlib import pyplot as plt
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)
data = client.open_by_key("1hD1BHyROsePmlJP6h7IFvuBjFrpoJkldpbL3l1cqe_4")
switcher = True

while switcher:
    user_input = input(
        "Оберіть потрібну інформацію:\n1 - Створити google sheet файл витрат часу на місяці\n2 - Переглянути графік часу"""
        "\n3 - Зробити новий аркуш (Якщо немає)""\n4 - Вийти\nВаш вибір? ")
    if not user_input or user_input.isalpha():
        print("Ви ввели не вірне значення")

    if user_input == "1":
        data = client.open_by_key("1hD1BHyROsePmlJP6h7IFvuBjFrpoJkldpbL3l1cqe_4")
        worksheet = data.sheet1
        Month = ["Mar", "Apr", "May", "Jun", "Jul"]
        Studying = ["20", "23", "24.5", "25", "26"]
        Hobby = ["30", "31", "31.3", "32", "32.4"]
        dataframe = pd.DataFrame(list(zip(Month, Studying, Hobby)),
                                 columns=['Month', 'Studying', 'Hobby'])
        worksheet.update([dataframe.columns.values.tolist()] + dataframe.values.tolist())
        print("Можешь зайти у google sheet і подивитися на результат")

    if user_input == "2":
        Month = ["Mar", "Apr", "May", "Jun", "Jul"]
        Studying = ["20", "23", "24.5", "25", "26"]
        Hobby = ["30", "31", "31.3", "32", "32.4"]
        x_indexes = range(len(Month))

        plt.bar(x_indexes, Studying, width=0.4, align='center', label='Study')

        hobby_shift = [x + 0.4 for x in x_indexes]

        plt.bar(hobby_shift, Hobby, width=0.4, align='center', label='Hobby')

        plt.xlabel('Місяці')
        plt.ylabel('Години')
        plt.title('Стовпчаста діаграма')
        plt.xticks(x_indexes, Month)
        plt.xticks(x_indexes, Month)

        plt.legend()

        plt.show()

    if user_input == "3":
        worksheet = data.add_worksheet(title='Test', rows=100, cols=100)
        print("Новий файл зроблено")

    if user_input == "4":
        switcher = False
