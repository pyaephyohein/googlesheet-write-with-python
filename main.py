from datetime import date
import json
import os
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import dotenv
import datetime
import time
dotenv.load_dotenv()

promeurl500 = os.getenv("prometheus_url_500")
promeurl504 = os.getenv("prometheus_url_504")
sheet_title = os.getenv('sheet_title')
json500_data = requests.get(promeurl500).json()
json504_data = requests.get(promeurl504).json()
sheet_name = os.getenv('sheet_name')


fhc500 = json500_data['data']['result'][0]['value'][1]
fhc504 = json504_data['data']['result'][0]['value'][1]


googleapis = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
credentials = ServiceAccountCredentials.from_json_keyfile_name("secret.json", googleapis)
file = gspread.authorize(credentials) 
sheet = file.open(sheet_title) 
sheet_select = tuple(sheet)[0]  

raw_date_today = date.today()
date_today = str(raw_date_today)
hour_time = time.strftime('%H:%M:%S')

sheet_select.append_row([date_today, hour_time, fhc500, fhc504])

