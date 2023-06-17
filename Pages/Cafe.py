# import plotly.express as px
import streamlit as sl
import pandas as pd
# from PIL import Image
from streamlit_extras.app_logo import add_logo
import datetime
from PIL import Image
import os

fries = Image.open('C:/Users/Cheek/PycharmProjects/GTC/media/fries.png')
mango_shake = Image.open('C:/Users/Cheek/PycharmProjects/GTC/media/mago_shake.png')
banana_sahke = Image.open('C:/Users/Cheek/PycharmProjects/GTC/media/Banana shake.png')
burger = Image.open('C:/Users/Cheek/PycharmProjects/GTC/media/burger.png')
coffee = Image.open('C:/Users/Cheek/PycharmProjects/GTC/media/coffee.png')
tea = Image.open('C:/Users/Cheek/PycharmProjects/GTC/media/tea.png')
sandwhich = Image.open('C:/Users/Cheek/PycharmProjects/GTC/media/Sandwhich.png')
biscuits = Image.open('C:/Users/Cheek/PycharmProjects/GTC/media/Biscuits.png')
nuggets = Image.open('C:/Users/Cheek/PycharmProjects/GTC/media/nuggets.png')
hotshots = Image.open('C:/Users/Cheek/PycharmProjects/GTC/media/hotshots.png')

date = datetime.datetime.now()
total_daily_rev = 0


def add_order(customer_name, customer_room, customer_number, amount_paid, total_bill, bal, serial):
    new_data = pd.DataFrame({"Serial": serial,
                             "Name": customer_name,
                             "Room": customer_room,
                             "Phone No": customer_number,
                             "Amount Paid": amount_paid,
                             "Total Bill": total_bill,
                             "Bill Due": bal}, index=[1])

    # read  file content
    reader = pd.read_excel(f'D:\Work\Python project\GTC\GTC\Pages\Cafe.xlsx')

    # create writer object
    # used engine='openpyxl' because append operation is not supported by xlsxwriter
    writer = pd.ExcelWriter(f'D:\Work\Python project\GTC\GTC\Pages\Cafe.xlsx', engine='openpyxl', mode='a',
                            if_sheet_exists="overlay")

    # append new dataframe to the Excel sheet
    new_data.to_excel(writer, index=False, header=False, startrow=len(reader) + 1)

    # close file
    writer.close()


# Open and Collect Cafe menu
cafe_menu = pd.read_excel("D:\Work\Python project\GTC\GTC\Pages\Cafe Menu.xlsx")

item_name = cafe_menu.loc[:, "Name"]
item_price = cafe_menu.loc[:, "Price"]
item_cost = cafe_menu.loc[:, "Cost"]

# Open and collect monthly cafe sales
cafe_data = pd.read_excel("D:\Work\Python project\GTC\GTC\Pages\Cafe.xlsx")

order_number = cafe_data.loc[:, "Serial"]
buyer_name = cafe_data.loc[:, "Name"]
room = cafe_data.loc[:, "Room"]
phone_no = cafe_data.loc[:, "Phone No"]
price = cafe_data.loc[:, "Amount Paid"]
total_rev = cafe_data.loc[:, "Total Bill"]
bill_due = cafe_data.loc[:, "Bill Due"]


def add_logo1():

    add_logo("logo.png", height=80)
    sl.markdown(
        """
        <style>

            [data-testid="stSidebarNav"]::before {
                content: "Gems Trade Center";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 20px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


sl.set_page_config(page_title="TradeCo Inc.", layout="wide")
sl.header('Café Dashboard')
add_logo1()

for i in range(len(total_rev)):
    total_daily_rev += total_rev[i]

with sl.container():
    with open('style.css') as f:
        sl.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    col1, col2, col3 = sl.columns(3)

    with col1:
        sl.write("Total Profit this Daily")
        sl.subheader("$1000")
        import streamlit as st

    with col2:
        sl.write("Growth comparing Yesterday")
        sl.subheader("80%")

    with col3:
        sl.write("Date")
        sl.subheader(f'{date.strftime("%d")} {date.strftime("%B")} {date.year}')
sl.progress(int(total_daily_rev / 100), "Daily Cafe Target Rs 1000")
sl.write(" ")
sl.line_chart(pd.DataFrame({"Serial": order_number, "Total Bill": total_rev}), x="Serial", y="Total Bill")
sl.write(" ")

with sl.container():
    with open('style.css') as f:
        sl.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    col1, col2, col3 = sl.columns(3)

    with col1:
        sl.write("Total Profit this Daily")
        sl.subheader("$1000")
        import streamlit as st

    with col2:
        sl.write("Growth comparing Yesterday")
        sl.subheader("80%")

    with col3:
        sl.write("Date")
        sl.subheader(f'{date.strftime("%d")} {date.strftime("%B")} {date.year}')
sl.progress(total_daily_rev / 10000, "Monthly Cafe Target Rs 10000")
sl.write(" ")
sl.line_chart(pd.DataFrame({"Serial": order_number, "Total Bill": total_rev}), x="Serial", y="Total Bill")

with open('style.css') as f:
    sl.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    Menu_row_1 = []
    Menu_row_1 = sl.columns(3)

    with Menu_row_1[0]:
        sl.image(fries, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB",
                 output_format="auto")

        input_Small_Pizza = int(sl.number_input("---------------------- Small Pizza ----------------------"))

    with Menu_row_1[1]:
        sl.image(mango_shake, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB",
                 output_format="auto")

        input_Medium_Pizza = int(sl.number_input("------- Medium Pizza -------"))

    with Menu_row_1[2]:
        sl.image(banana_sahke, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB",
                 output_format="auto")

        input_Large_Pizza = int(sl.number_input("------- Large Pizza -------"))

    Menu_row_2 = []
    Menu_row_2 = sl.columns(3)

    with Menu_row_2[0]:
        sl.image(coffee, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB",
                 output_format="auto")

        input_Coffee = int(sl.number_input("------- Coffee -------"))

    with Menu_row_2[1]:
        sl.image(tea, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB",
                 output_format="auto")

        input_Tea = int(sl.number_input("------- Tea -------"))

    with Menu_row_2[2]:
        sl.image(tea, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB",
                 output_format="auto")

        input_Green_Tea = int(sl.number_input("------- Green Tea -------"))

    Menu_row_3 = []
    Menu_row_3 = sl.columns(3)

    with Menu_row_3[0]:
        sl.image(burger, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB",
                 output_format="auto")

        input_Burger = int(sl.number_input("------- Burger -------"))

    with Menu_row_3[1]:
        sl.image(sandwhich, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB",
                 output_format="auto")

        input_Sandwich = int(sl.number_input("------- Sandwich -------"))

    with Menu_row_3[2]:
        test1 = sl.image(biscuits, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB",
                                    output_format="auto")

        input_biscut = int(sl.number_input("------- Biscuits -------"))

    Menu_row_4 = []
    Menu_row_4 =sl.columns(2)

    with Menu_row_4[0]:
        sl.image(hotshots, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB",
                 output_format="auto")

        input_hotshot = int(sl.number_input("------- Hotshot -------"))

    with Menu_row_4[1]:
        sl.image(nuggets, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB",
                 output_format="auto")

        input_nuggets = int(sl.number_input("------- Nuggets -------"))


sl.subheader("----------------------------------------------------------------------------------------------------"
             "-------------------------------------------")

total_bill = 0

col1, col2 = sl.columns(2)
with col1:
    customer_name = sl.text_input('Name:', '')
    customer_room = sl.text_input('Room No:', '')

with col2:
    customer_number = sl.text_input('Phone Number:', '')
    amount_paid = sl.text_input('Amount Paid:', '')

col1, col2 = sl.columns(2)
with col1:
    if sl.button("Place Order"):
        if input_Small_Pizza > 0:
            sl.subheader(f"{item_name[5]} ----------- Price: {item_price[5]} ---------- QTY: {input_Small_Pizza}")
            total_bill += (item_price[5]*input_Small_Pizza)
        if input_Medium_Pizza > 0:
            sl.subheader(f"{item_name[6]} ----------- Price: {item_price[6]}------------{input_Medium_Pizza}")
            total_bill += (item_price[6] * input_Medium_Pizza)
        if input_Large_Pizza > 0:
            sl.subheader(f"{item_name[7]} ----------- Price: {item_price[7]}------------{input_Large_Pizza}")
            total_bill += (item_price[7] * input_Large_Pizza)
        if input_Coffee > 0:
            sl.subheader(f"{item_name[2]} ----------- Price: {item_price[2]}------------{input_Coffee}")
            total_bill += (item_price[2] * input_Coffee)
        if input_Tea > 0:
            sl.subheader(f"{item_name[0]} ----------- Price: {item_price[0]}------------{input_Tea}")
            total_bill += (item_price[0] * input_Tea)
        if input_Green_Tea > 0:
            sl.subheader(f"{item_name[1]} ----------- Price: {item_price[1]}------------{input_Green_Tea}")
            total_bill += (item_price[1] * input_Green_Tea)
        if input_Burger > 0:
            sl.subheader(f"{item_name[8]} ----------- Price: {item_price[8]}------------{input_Burger}")
            total_bill += (item_price[8] * input_Burger)
        if input_Sandwich > 0:
            sl.subheader(f"{item_name[4]} ----------- Price: {item_price[4]}------------{input_Sandwich}")
            total_bill += (item_price[4] * input_Sandwich)
        sl.header(f"Total Bill: --------------------- {total_bill}")

with col2:
    if sl.button("Submit"):
        if input_Small_Pizza > 0:
            total_bill += (item_price[5] * input_Small_Pizza)
        if input_Medium_Pizza > 0:
            total_bill += (item_price[6] * input_Medium_Pizza)
        if input_Large_Pizza > 0:
            total_bill += (item_price[7] * input_Large_Pizza)
        if input_Coffee > 0:
            total_bill += (item_price[2] * input_Coffee)
        if input_Tea > 0:
            total_bill += (item_price[0] * input_Tea)
        if input_Green_Tea > 0:
            total_bill += (item_price[1] * input_Green_Tea)
        if input_Burger > 0:
            total_bill += (item_price[8] * input_Burger)
        if input_Sandwich > 0:
            total_bill += (item_price[4] * input_Sandwich)
        bal = int(amount_paid) - total_bill
        serial = len(order_number) + 1
        token = (f"Name ------- {customer_name}\n"
                  f"Room ------- {customer_room}\n"
                  f"Phone ------- {customer_number}\n"
                  f"Paid ------- {amount_paid}\n"
                  f"Total ------- {total_bill}\n"
                  f"Balance ------- {bal}\n"
                  f"Order No. ------- {serial}")
        more_lines = ["        GTC       ", token, "\n-------GTC Cafe------"]
        order_file = f"{serial}.txt"
        with open(order_file, 'a') as f:
            f.write('\n'.join(more_lines))
        os.startfile(f"{serial}.txt", "print")
        print(token)
        add_order(customer_name, customer_room, customer_number, amount_paid, total_bill, bal, serial)