# import plotly.express as px
import streamlit as sl
import pandas as pd
# from PIL import Image
# import time
#from streamlit_extras.app_logo import add_logo
import datetime

import pickle
from pathlib import Path
#import streamlit_authenticator as slauth


status = False
start = 101
end = 111

date = datetime.datetime.now()

excel_file = 'Pages/Book1.xlsx'
data = pd.read_excel(excel_file)

office_ID = data.loc[:, "Office ID"]
tenant_name = data.loc[:, "Tenant name"]
tenant_number = data.loc[:, "Tenant number"]
cnic = data.loc[:, "CNIC"]
business_name = data.loc[:, "Business name"]
email = data.loc[:, "Email"]
rent = data.loc[:, "Rent"]
issue_date = data.loc[:, "Issue Date"]

excel_file = "Pages/Parking.xlsx"
data_parking = pd.read_excel(excel_file)
parking_id = data_parking.loc[:, "Parking ID"]


def add_logo1():
    add_logo("logo.png", height=120)
    sl.markdown(
        """
        <style>

            [data-testid="stSidebarNav"]::before {
                content: "Gems Trade Center";
                margin-left: 30px;
                margin-top: 10px;
                font-size: 20px;
                position: relative;
                top: 80px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


sl.set_page_config(page_title="Gems Trade Center", layout="wide")


names = ["Osama Khan", "Dev Admin"]
usernames = ["admin", "Dev"]

credentials = {"usernames":{}}


file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)
    for un, name, pw in zip(usernames, names, hashed_passwords):
        user_dict = {"name": name, "password": pw}
        credentials["usernames"].update({un: user_dict})

    authenticator = slauth.Authenticate(credentials, "dash_cookie", "abcde", cookie_expiry_days=30)


name, authentication_status, username = authenticator.login("login", "main")

if authentication_status == False:
    sl.error("Username/Password in incorrect")

if authentication_status == None:
    sl.warning("Please enter credentias")

if authentication_status:

    sl.header('GTC Dashboard')
    add_logo1()
    authenticator.logout("Logout", "sidebar")
    status = authentication_status

    with sl.container():
        with open('style.css') as f:
            sl.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        col1, col2, col3 = sl.columns(3)

        with col1:
            sl.write("Total Profit this month")
            sl.subheader("$1000")
            import streamlit as st

        with col2:
            sl.write("Growth comparing last month")
            sl.subheader("80%")

        with col3:
            sl.write("Date")
            sl.subheader(f'{date.strftime("%d")} {date.strftime("%B")} {date.year}')

    with sl.container():
        chart1, chart2 = sl.columns(2)

        with chart1:
            sl.subheader("Cafe Monthly")
            sl.markdown("""<style>
                    [data-testid="css-10trblm e16nr0p30"]::before {
                    content: "Gems Tradec Center";
                    font-size: 20px;
                }
            
            </style>""",
                        unsafe_allow_html=True,)
            sl.line_chart(data_parking, x="Parking ID", y="Fee")

        with chart2:
            sl.subheader("Rent Monthly")
            sl.line_chart(data, x="Issue Date", y="Rent")

    with sl.container():
        sl.subheader("Total Rent received This month: ")
        sl.progress(55)
        rooms = []
        rooms = sl.columns(7)

        for j in rooms:
            with j:
                for i in range(start, end):
                    if str(i) in str(office_ID):
                        sl.subheader(f":green[{i}]")
                    else:
                        sl.subheader(f":red[{i}]")
                        # (f":blue[{i}]")
                start += 100
                end += 100

    with sl.container():
        sl.subheader("Total Parking Fee collected: ")
        sl.progress(20)
        parking_space = []
        parking_space = sl.columns(5)

        for j in parking_space:
            with j:
                for i in range(start-800, end -805):
                    if "P"+str(i) in str(parking_id):
                        sl.subheader(f":red[P{i}]")
                    else:
                        sl.subheader(f":green[P{i}]")
                        # sl.subheader(f":blue[P{i}]")
                start += 5
                end += 5

    with sl.container():
        sl.subheader("Total Cafe monthly target: ")
        sl.progress(90)
        sl.line_chart(pd.DataFrame({"Issue Date": issue_date, "Rent": rent}), x="Issue Date", y="Rent")
