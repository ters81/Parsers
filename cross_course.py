from requests import get
from bs4 import BeautifulSoup
from tkinter import Tk, Entry, CENTER, DISABLED, Label


from tkinter import PhotoImage


def make_button(text):
    return Label(text=text, font='arial 15', master=win, borderwidth=5)


link = "https://privatbank.ua/"
responce = get(link).text
soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', id="widget")

EUR_sell = block.find('td', id="EUR_sell").text.strip()
EUR_buy = block.find('td', id="EUR_buy").text.strip()

USD_sell = block.find('td', id="USD_sell").text.strip()
USD_buy = block.find('td', id="USD_buy").text.strip()

cross_course = round(float(EUR_sell) / float(USD_buy), 2)

win = Tk()

# Размеры окна
win.geometry("350x200")
win.resizable(False, False)

# Размещение окна по центру экрана
win.update_idletasks()
s = win.geometry()
s = s.split('+')
s = s[0].split('x')
s_win = s[0]
width_win = int(s[0])
height_win = int(s[1])
w = win.winfo_screenwidth()
h = win.winfo_screenheight()
w = w // 2
h = h // 2
w = w - width_win // 2
h = h - height_win // 2
win.geometry(f'+{w}+{h}')

# Внешний вид окна
win.config(bg='#ffffff', relief='raised')
# Название окна
win.title('Кросс Курс')

photo = PhotoImage(file='PB3.png')
win.iconphoto(False, photo)


make_button('Купівля').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_button('Продаж').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_button('EUR').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_button('USD').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_button('Кросс Курс').grid(row=4, column=0, stick='wens', padx=5, pady=5)

entry_EUR_buy = Entry(master=win, font='arial 15', borderwidth=5, justify=CENTER)
entry_EUR_buy.grid(row=2, column=1, stick='wens', padx=5, pady=5)
entry_EUR_buy.insert(0, EUR_buy)
entry_EUR_buy['state'] = DISABLED

entry_EUR_sell = Entry(master=win, font='arial 15', borderwidth=5, justify=CENTER)
entry_EUR_sell.grid(row=2, column=2, stick='wens', padx=5, pady=5)
entry_EUR_sell.insert(0, EUR_sell)
entry_EUR_sell['state'] = DISABLED

entry_USD_buy = Entry(master=win, font='arial 15', borderwidth=5, justify=CENTER)
entry_USD_buy.grid(row=3, column=1, stick='wens', padx=5, pady=5)
entry_USD_buy.insert(0, USD_buy)
entry_USD_buy['state'] = DISABLED

entry_USD_sell = Entry(master=win, font='arial 15', borderwidth=5, justify=CENTER)
entry_USD_sell.grid(row=3, column=2, stick='wens', padx=5, pady=5)
entry_USD_sell.insert(0, USD_sell)
entry_USD_sell['state'] = DISABLED

entry_cross_course = Entry(master=win, font=('arial', 15, 'bold'), borderwidth=5, justify=CENTER)
entry_cross_course.grid(row=4, column=1, stick='wens', padx=5, pady=5, columnspan=2)
entry_cross_course.insert(0, cross_course)
entry_cross_course['state'] = DISABLED

win.grid_columnconfigure(0, weight=0)
win.grid_columnconfigure(1, weight=1)
win.grid_columnconfigure(2, weight=1)

win.mainloop()
