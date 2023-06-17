# # import plotly.express as px
import streamlit as sl
# import pandas as pd
# # from PIL import Image
# # from streamlit_extras.app_logo import add_logo
# import datetime
# from os.path import exists
# import xlsxwriter
# import Dashboard
#
# status = Dashboard.return_call()
# date = datetime.datetime.now()
#
# if status:
#
#     def add_new_office():
#         # input new office
#         new_ID = input("Office ID: ")
#         new_tenant_name = input("Name: ")
#         new_tenant_number = input("Contact Number: ")
#         new_cnic = input("Tenant ID: ")
#         new_business_name = input("Business Name: ")
#         new_email = input("Email: ")
#         new_rent = input("Rent: ")
#         new_advance = input("Advance Paid: ")
#         new_issue_date = input("Issue Date: ")
#
#         new_data = pd.DataFrame({"Office ID": new_ID,
#                                  "Tenant name": new_tenant_name,
#                                  "Tenant number": new_tenant_number,
#                                  "CNIC": new_cnic,
#                                  "Business name": new_business_name,
#                                  "Email": new_email,
#                                  "Rent": new_rent,
#                                  "Advance": new_advance,
#                                  "Issue Date": new_issue_date}, index=[1])
#
#         # read  file content
#         reader = pd.read_excel(f'{date.month}_Rents_data.xlsx')
#
#         # create writer object
#         # used engine='openpyxl' because append operation is not supported by xlsxwriter
#         writer = pd.ExcelWriter(f'Book1.xlsx', engine='openpyxl', mode='a', if_sheet_exists="overlay")
#
#         # append new dataframe to the Excel sheet
#         new_data.to_excel(writer, index=False, header=False, startrow=len(reader) + 1)
#
#         # close file
#         writer.close()
#
#
#     def check_total_rent():
#         offices_data = pd.read_excel('Book1.xlsx')
#
#
#
#     date = datetime.datetime.now()
#
#     excel_file = 'Book1.xlsx'
#     offices_data = pd.read_excel(excel_file)
#
#     if not exists(f'{date.month}_Rents_data.xlsx'):
#         workbook = xlsxwriter.Workbook(f'{date.month}_Rents_data.xlsx')
#         worksheet = workbook.add_worksheet()
#
#         # Start from the first cell.
#         # Rows and columns are zero indexed.
#         row = 0
#         column = 0
#
#         content = ["Office ID", "Tenant name", "Tenant number", "CNIC",
#                    "Business name", "Email", "Rent", "Issue Date"]
#
#         # iterating through content list
#         for item in content:
#             # write operation perform
#             worksheet.write(row, column, item)
#
#             # incrementing the value of row by one
#             # with each loop.
#             column += 1
#
#         workbook.close()
#         paid_data1 = pd.read_excel(f'{date.month}_Rents_data.xlsx')
#     else:
#         paid_data1 = pd.read_excel(f'{date.month}_Rents_data.xlsx')
#
#     office_ID = offices_data.loc[:, "Office ID"]
#     tenant_name = offices_data.loc[:, "Tenant name"]
#     tenant_number = offices_data.loc[:, "Tenant number"]
#     cnic = offices_data.loc[:, "CNIC"]
#     business_name = offices_data.loc[:, "Business name"]
#     email = offices_data.loc[:, "Email"]
#     rent = offices_data.loc[:, "Rent"]
#     advance = offices_data.loc[:, "Advance"]
#     issue_date = offices_data.loc[:, "Issue Date"]
#
#     paid_data = paid_data1["Office ID"]
#     paid_data2 = paid_data1["Rent"]
#     paid_ID = []
#     rent_paid1 = 0
#     total_rent = 0
#     for i in range(0, len(paid_data)):
#         paid_ID.append(int(paid_data[i]))
#         rent_paid1 += int(paid_data2[i])
#
#     office_ID_paid = []
#     tenant_name_paid = []
#     tenant_number_paid = []
#     cnic_paid = []
#     business_name_paid = []
#     email_paid = []
#     rent_paid = []
#     rent_date_paid = []
#
#     while True:
#         office_ID_input = input("Please enter Office ID: ")
#         if office_ID_input in office_ID:
#             if int(office_ID_input) not in paid_ID:
#                 for i in range(len(office_ID)):
#                     total_rent += rent[i]
#                     if int(office_ID_input) == int(office_ID[i]):
#                         print(f'Due Rent: {rent[i]}')
#                         rent_input = input("Please enter Paid Rent: ")
#                         date_input = datetime.datetime.now().date()
#                         break
#             else:
#                 print("Rent Already paid")
#                 continue
#         else:
#             print("seller not in Database.")
#             new_office = input("Do you want to assign a new office ID? (y/n): ")
#             if new_office == "y":
#                 add_new_office()
#
#             elif new_office == "n":
#                 print("Thank you")
#                 break
#             else:
#                 print("Wrong Input")
#
#     for i in range(len(office_ID)):
#         if int(office_ID_input) == office_ID[i]:
#             office_ID_paid.append(office_ID[i])
#             tenant_name_paid.append(tenant_name[i])
#             tenant_number_paid.append(tenant_number[i])
#             cnic_paid.append(cnic[i])
#             business_name_paid.append(business_name[i])
#             email_paid.append(email[i])
#             rent_paid.append(rent_input)
#             rent_date_paid.append(date_input)
#
#     df = pd.DataFrame({"Office ID": office_ID_paid,
#                        "Tenant name": tenant_name_paid,
#                        "Tenant number": tenant_number_paid,
#                        "CNIC": cnic_paid,
#                        "Business name": business_name_paid,
#                        "Email": email_paid,
#                        "Rent": rent_paid,
#                        "Issue Date": rent_date_paid})
#
#     # read  file content
#     reader = pd.read_excel(f'{date.month}_Rents_data.xlsx')
#
#     # create writer object
#     # used engine='openpyxl' because append operation is not supported by xlsxwriter
#     writer = pd.ExcelWriter(f'{date.month}_Rents_data.xlsx', engine='openpyxl', mode='a', if_sheet_exists="overlay")
#
#     # append new dataframe to the Excel sheet
#     df.to_excel(writer, index=False, header=False, startrow=len(reader) + 1)
#
#     # close file
#     writer.close()
#
#     print(rent_paid1, total_rent)
#
#     # def add_logo1():
#     #
#     #     add_logo("logo.png", height=80)
#     #     sl.markdown(
#     #         """
#     #         <style>
#     #
#     #             [data-testid="stSidebarNav"]::before {
#     #                 content: "Gems Tradec Center";
#     #                 margin-left: 20px;
#     #                 margin-top: 20px;
#     #                 font-size: 30px;
#     #                 position: relative;
#     #                 top: 100px;
#     #             }
#     #         </style>
#     #         """,
#     #         unsafe_allow_html=True,
#     #     )
#     #
#     #
#     # sl.set_page_config(page_title="TradeCo Inc.")
#     # sl.header('Offices Dashboard')
#     # add_logo1()

from streamlit_card import card

hasClicked = card(
  title="Hello World!",
  text="Some description",
  image="http://placekitten.com/200/300",
)

if hasClicked:
    sl.subheader("Worked")

