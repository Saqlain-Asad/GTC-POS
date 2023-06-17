# import plotly.express as px
# import streamlit as sl
import pandas as pd
# from PIL import Image
# from streamlit_extras.app_logo import add_logo
from os.path import exists
import xlsxwriter
import datetime
import Dashboard

status = Dashboard.return_call()
date = datetime.datetime.now()

if status:
    def add_parking():
        # input from user.
        new_parking_id = input("Enter Parking ID: ")
        new_office_id = input("Enter Office ID: ")

        if new_parking_id not in str(parking_id):
            for i in range(len(office_ID)):
                if new_office_id == str(office_ID[i]):
                    new_car_name = input("Enter Car name and model: ")
                    new_car_reg_number = input("Enter Car registration Number: ")
                    new_parking_fee = input("Enter parking Fee: ")

                    # New data frame for excel sheet
                    new_data = pd.DataFrame({"Parking ID": new_parking_id,
                                             "Office ID": new_office_id,
                                             "Car Name": new_car_name,
                                             "Car number": new_car_reg_number,
                                             "Fee": new_parking_fee}, index=[1])

                    # read  file content
                    reader = pd.read_excel('Parking.xlsx')

                    # create writer object
                    # used engine='openpyxl' because append operation is not supported by xlsxwriter
                    writer = pd.ExcelWriter('Parking.xlsx', engine='openpyxl', mode='a', if_sheet_exists="overlay")

                    # append new dataframe to the Excel sheet
                    new_data.to_excel(writer, index=False, header=False, startrow=len(reader) + 1)

                    # close file
                    writer.close()
                    break
            else:
                print(" 404 : Office ID not found")
        else:
            print("parking Reserved!")


    def edit_parking():
        parking_id_input = input("Enter Parking ID you wish to edit: ")
        if parking_id_input in str(parking_id):
            for i in range(len(parking_id)):
                if parking_id_input == parking_id[i]:
                    print(f"Please Input All required fields for Parking ID: {parking_id_input}\n")
                    office_ID[i] = input("Enter New Office ID: ")
                    car_name[i] = input("Enter New Car name: ")
                    car_reg[i] = input("Enter New Car registration Number: ")
                    park_fee[i] = input("Enter New Parking Fee: ")

                    new_data = pd.DataFrame({"Parking ID": parking_id,
                                             "Office ID": office_id,
                                             "Car Name": car_name,
                                             "Car number": car_reg,
                                             "Fee": park_fee})
                    new_data = new_data.set_index("Parking ID")
                    new_data.to_excel('Parking.xlsx')
        else:
            print("Office ID either not assigned or is wrong!! 🤬")


    def add_parking_fee():
        edit_parking_id = input("Enter Parking ID: ")
        if edit_parking_id in str(parking_id):
            if not exists(f'{date.month}_Parking_fee_data.xlsx'):
                workbook = xlsxwriter.Workbook(f'{date.month}_Parking_fee_data.xlsx')
                worksheet = workbook.add_worksheet()

                # Start from the first cell.
                # Rows and columns are zero indexed.
                row = 0
                column = 0

                content = ["Parking ID", "Office ID", "Car name", "Car number", "Fee", "Date"]

                # iterating through content list
                for item in content:
                    # write operation perform
                    worksheet.write(row, column, item)

                    # incrementing the value of row by one
                    # with each loop.
                    column += 1

                workbook.close()
                rent_data = pd.read_excel(f'{date.month}_Parking_fee_data.xlsx')
            else:
                rent_data = pd.read_excel(f'{date.month}_Parking_fee_data.xlsx')

            paid_parking_ID = rent_data["Parking ID"]

            if edit_parking_id in str(paid_parking_ID):
                print("Fee paid!!")

            else:
                fee_input = input("input fee: ")
                parking_id_paid = []
                office_ID_paid = []
                car_name_paid = []
                car_reg_paid = []
                fee_paid = []
                fee_date_paid = []
                for i in range(len(parking_id)):
                    if edit_parking_id == str(parking_id[i]):
                        print("works")
                        parking_id_paid.append(parking_id[i])
                        office_ID_paid.append(office_ID[i])
                        car_name_paid.append(car_name[i])
                        car_reg_paid.append(car_reg[i])
                        fee_paid.append(fee_input)
                        fee_date_paid.append(datetime.datetime.now().date())

                # New data frame for excel sheet
                new_data = pd.DataFrame({"Parking ID": parking_id_paid,
                                         "Office ID": office_ID_paid,
                                         "Car Name": car_name_paid,
                                         "Car number": car_reg_paid,
                                         "Fee": fee_paid,
                                         "Date": fee_date_paid})

                # read  file content
                reader = pd.read_excel(f'{date.month}_Parking_fee_data.xlsx')

                # create writer object
                # used engine='openpyxl' because append operation is not supported by xlsxwriter
                writer = pd.ExcelWriter(f'{date.month}_Parking_fee_data.xlsx', engine='openpyxl', mode='a', if_sheet_exists="overlay")

                # append new dataframe to the Excel sheet
                new_data.to_excel(writer, index=False, header=False, startrow=len(reader) + 1)

                # close file
                writer.close()


    def edit_parking_fee():
        parking_ID_input = input("Enter office ID you wish to edit: ")
        fee_data = pd.read_excel(f'{date.month}_Parking_fee_data.xlsx')

        paid_office_ID = fee_data["Parking ID"]
        paid_rent = fee_data["Fee"]

        if parking_ID_input in str(paid_office_ID):
            new_fee = input("Input new Fee Information: ")
            for i in range(len(paid_office_ID)):
                if parking_ID_input == str(paid_office_ID[i]):
                    print("Works")
                    paid_rent[i] = new_fee

            new_data = pd.DataFrame({"Parking ID": fee_data["Parking ID"],
                                    "Office ID": fee_data["Office ID"],
                                     "Car name": fee_data["Car name"],
                                     "Car number": fee_data["Car number"],
                                     "Fee": paid_rent,
                                     "Date": datetime.datetime.now().date()})
            new_data = new_data.set_index("Parking ID")
            new_data.to_excel(f'{date.month}_Parking_fee_data.xlsx')

        else:
            print("Office ID either not assigned or is wrong!! 🤬")


    parking_data = pd.read_excel("Parking.xlsx")

    parking_id = parking_data.loc[:, "Parking ID"]
    office_id = parking_data.loc[:, "Office ID"]
    car_name = parking_data.loc[:, "Car Name"]
    car_reg = parking_data.loc[:, "Car number"]
    park_fee = parking_data.loc[:, "Fee"]

    offices_data = pd.read_excel("Book1.xlsx")

    # collect and categorize data
    office_ID = offices_data.loc[:, "Office ID"]

    choice = input("Choice: ")

    if choice == "1":
        edit_parking()
    elif choice == "2":
        add_parking()
    elif choice == "3":
        add_parking_fee()
    elif choice == "4":
        edit_parking_fee()
    elif choice == "5":
        print(parking_data)
    elif choice == "6":
        print(pd.read_excel(f'{date.month}_Parking_fee_data.xlsx'))
    # def add_logo1():
    #
    #     add_logo("logo.png", height=80)
    #     sl.markdown(
    #         """
    #         <style>
    #
    #             [data-testid="stSidebarNav"]::before {
    #                 content: "Gems Tradec Center";
    #                 margin-left: 20px;
    #                 margin-top: 20px;
    #                 font-size: 30px;
    #                 position: relative;
    #                 top: 100px;
    #             }
    #         </style>
    #         """,
    #         unsafe_allow_html=True,
    #     )
    #
    #
    # sl.set_page_config(page_title="TradeCo Inc.")
    # sl.header('Parking Dashboard')
    # add_logo1()
