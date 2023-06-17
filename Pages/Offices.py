# import plotly.express as px
import streamlit as sl
import pandas as pd
# from PIL import Image
from streamlit_extras.app_logo import add_logo
from os.path import exists
import xlsxwriter
import datetime
from streamlit_card import card
import base64

date = datetime.datetime.now()
start = 101
end = 111

if True:

    def add_new_office():
        # Input from user
        new_ID = input("Office ID: ")
        new_tenant_name = input("Name: ")
        new_tenant_number = input("Contact Number: ")
        new_cnic = input("Tenant ID: ")
        new_business_name = input("Business Name: ")
        new_email = input("Email: ")
        new_rent = input("Rent: ")
        new_advance = input("Advance Paid: ")
        new_issue_date = datetime.datetime.now().date()

        # New data frame for excel sheet
        new_data = pd.DataFrame({"Office ID": new_ID,
                                 "Tenant name": new_tenant_name,
                                 "Tenant number": new_tenant_number,
                                 "CNIC": new_cnic,
                                 "Business name": new_business_name,
                                 "Email": new_email,
                                 "Rent": new_rent,
                                 "Advance": new_advance,
                                 "Issue Date": new_issue_date}, index=[1])

        # read  file content
        reader = pd.read_excel(f'{date.month}_Rents_data.xlsx')

        # create writer object
        # used engine='openpyxl' because append operation is not supported by xlsxwriter
        writer = pd.ExcelWriter(f'Book1.xlsx', engine='openpyxl', mode='a', if_sheet_exists="overlay")

        # append new dataframe to the Excel sheet
        new_data.to_excel(writer, index=False, header=False, startrow=len(reader) + 1)

        # close file
        writer.close()


    def add_new_rent():
        office_ID_input = input("Enter Office ID: ")
        if office_ID_input in str(office_ID):
            if not exists(f'{date.month}_Rents_data.xlsx'):
                workbook = xlsxwriter.Workbook(f'{date.month}_Rents_data.xlsx')
                worksheet = workbook.add_worksheet()

                # Start from the first cell.
                # Rows and columns are zero indexed.
                row = 0
                column = 0

                content = ["Office ID", "Tenant name", "Tenant number", "CNIC",
                           "Business name", "Email", "Rent", "Issue Date"]

                # iterating through content list
                for item in content:
                    # write operation perform
                    worksheet.write(row, column, item)

                    # incrementing the value of row by one
                    # with each loop.
                    column += 1

                workbook.close()
                rent_data = pd.read_excel(f'{date.month}_Rents_data.xlsx')
            else:
                rent_data = pd.read_excel(f'{date.month}_Rents_data.xlsx')

            paid_office_ID = rent_data["Office ID"]
            paid_Rent = rent_data["Rent"]

            if office_ID_input in str(paid_office_ID):
                print("Rent paid!!")

            else:
                rent_input = input("Enter New rent")
                office_ID_paid = []
                tenant_name_paid = []
                tenant_number_paid = []
                cnic_paid = []
                business_name_paid = []
                email_paid = []
                rent_paid = []
                rent_date_paid = []
                for i in range(len(office_ID)):
                    if int(office_ID_input) == office_ID[i]:
                        office_ID_paid.append(office_ID[i])
                        tenant_name_paid.append(tenant_name[i])
                        tenant_number_paid.append(tenant_number[i])
                        cnic_paid.append(cnic[i])
                        business_name_paid.append(business_name[i])
                        email_paid.append(email[i])
                        rent_paid.append(rent_input)
                        rent_date_paid.append(datetime.datetime.now().date())

                df = pd.DataFrame({"Office ID": office_ID_paid,
                                   "Tenant name": tenant_name_paid,
                                   "Tenant number": tenant_number_paid,
                                   "CNIC": cnic_paid,
                                   "Business name": business_name_paid,
                                   "Email": email_paid,
                                   "Rent": rent_paid,
                                   "Issue Date": rent_date_paid})

                # read  file content
                reader = pd.read_excel(f'{date.month}_Rents_data.xlsx')

                # create writer object
                # used engine='openpyxl' because append operation is not supported by xlsxwriter
                writer = pd.ExcelWriter(f'{date.month}_Rents_data.xlsx', engine='openpyxl', mode='a',
                                        if_sheet_exists="overlay")

                # append new dataframe to the Excel sheet
                df.to_excel(writer, index=False, header=False, startrow=len(reader) + 1)

                # close file
                writer.close()
        else:
            print("Office ID either not assigned or is wrong!! 🤬")


    def edit_office():
        office_ID_input = int(input("Enter office ID you wish to edit: "))
        if office_ID_input in str(office_ID):
            for i in range(len(office_ID)):
                if office_ID_input == office_ID[i]:
                    print(office_ID_input)
                    for i in range(len(office_ID)):
                        if office_ID_input == office_ID[i]:
                            print(f"Please Input All required fields for Office ID: {office_ID_input}\n")
                            tenant_name[i] = input("Enter Name: ")
                            tenant_number[i] = input("\nEnter tenant number: ")
                            cnic[i] = input("\nEnter National ID information")
                            business_name[i] = input("\nEnter Business name: ")
                            email[i] = input("\nEnter User Email: ")
                            rent[i] = input("\nEnter Rent Information: ")
                            advance[i] = input("\nEnter Advance paid: ")
                            issue_date[i] = datetime.datetime.now().date()

                    new_data = pd.DataFrame({"Office ID": office_ID,
                                             "Tenant name": tenant_name,
                                             "Tenant number": tenant_number,
                                             "CNIC": cnic,
                                             "Business name": business_name,
                                             "Email": email,
                                             "Rent": rent,
                                             "Advance": advance,
                                             "Issue Date": issue_date})
                    new_data.to_excel('Book1.xlsx')

        else:
            print("Office ID either not assigned or is wrong!! 🤬")


    def edit_rent():
        office_ID_input = input("Enter office ID you wish to edit: ")
        rent_data = pd.read_excel(f'{date.month}_Rents_data.xlsx')

        paid_office_ID = rent_data["Office ID"]
        paid_rent = rent_data["Rent"]
        # name = rent_data["Tenant name"]
        # number = rent_data["Tenant number"]
        # CNIC = rent_data["CNIC"]
        # business_n = rent_data["Business"]
        # rent_email = rent_data["Email"]
        # new_date = datetime.datetime.now().date()

        if office_ID_input in str(paid_office_ID):
            new_rent = input("Input new rent Information: ")
            for i in range(len(paid_office_ID)):
                if office_ID_input == str(paid_office_ID[i]):
                    paid_rent[i] = new_rent

            new_data = pd.DataFrame({"Office ID": rent_data["Office ID"],
                                     "Tenant name": rent_data["Tenant name"],
                                     "Tenant number": rent_data["Tenant number"],
                                     "CNIC": rent_data["CNIC"],
                                     "Business name": rent_data["Business name"],
                                     "Email": rent_data["Email"],
                                     "Rent": paid_rent,
                                     "Issue Date": datetime.datetime.now().date()})
            new_data.to_excel(f'{date.month}_Rents_data.xlsx')
            print(new_data)
        else:
            print("Office ID either not assigned or is wrong!! 🤬")


    offices_data = pd.read_excel("Book1.xlsx")
    # print(offices_data)
    # collect and categorize data
    office_ID = offices_data.loc[:, "Office ID"]
    tenant_name = offices_data.loc[:, "Tenant name"]
    tenant_number = offices_data.loc[:, "Tenant number"]
    cnic = offices_data.loc[:, "CNIC"]
    business_name = offices_data.loc[:, "Business name"]
    email = offices_data.loc[:, "Email"]
    rent = offices_data.loc[:, "Rent"]
    advance = offices_data.loc[:, "Advance"]
    issue_date = offices_data.loc[:, "Issue Date"]


    # choice = input("Choice: ")
    #
    # if choice == "1":
    #     edit_office()
    # elif choice == "2":
    #     add_new_rent()
    # elif choice == "3":
    #     add_new_office()
    # elif choice == "4":
    #     edit_rent()
    # elif choice == "5":
    #     print(offices_data)
    # elif choice == "6":
    #     print(pd.read_excel(f'{date.month}_Rents_data.xlsx'))

    def add_logo1():

        add_logo("logo.png", height=80)
        sl.markdown(
            """
            <style>

                [data-testid="stSidebarNav"]::before {
                    content: "Gems Tradec Center";
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


    sl.set_page_config(layout="wide")
    with sl.container():
        with open('style.css') as f:
            sl.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        col1, col2, col3 = sl.columns(3)

        with col1:
            sl.write("Total Rent Collected June")
            sl.subheader("$1000")
            import streamlit as st

        with col2:
            sl.write("Total rent pending June")
            sl.subheader("80%")

        with col3:
            sl.write("Date")
            sl.subheader(f'{date.strftime("%d")} {date.strftime("%B")} {date.year}')

    excel_file = 'Pages/Book1.xlsx'
    data = pd.read_excel(excel_file)
    sl.subheader("Rent Monthly")
    sl.line_chart(data, x="Office ID", y="Rent")
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

    sl.header("Edit Room Info")
    col1, col2, col3 = sl.columns(3)
    with col1:
        with open("C:/Users/Cheek/PycharmProjects/GTC/media/add_room.png", "rb") as f:
            data = f.read()
            encoded = base64.b64encode(data)
        room_image = "data:image/png;base64," + encoded.decode("utf-8")

        add_room = card(
            title="Add Room",
            text="Add new Room to if available",
            image=room_image
        )

        if add_room:
            sl.subheader("Worked")

    with col2:
        with open("C:/Users/Cheek/PycharmProjects/GTC/media/add_rent.jpg", "rb") as f:
            data = f.read()
            encoded = base64.b64encode(data)
        room_image = "data:image/png;base64," + encoded.decode("utf-8")
        add_rent = add_room = card(
            title="Add Rent",
            text="Add new Rent",
            image=room_image
        )

        if add_room:
            sl.subheader("Worked")

    with col3:
        with open("C:/Users/Cheek/PycharmProjects/GTC/media/edit_room.jpg", "rb") as f:
            data = f.read()
            encoded = base64.b64encode(data)
        room_image = "data:image/png;base64," + encoded.decode("utf-8")

        change_room = add_room = card(
            title="Edit Room",
            text="Add new Room to if available",
            image=room_image
        )

if add_room:
    sl.subheader("Worked")
