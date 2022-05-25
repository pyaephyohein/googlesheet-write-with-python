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

promeurl = os.getenv("prometheus_url")
sheet_title = os.getenv('sheet_title')
json_data = requests.get(promeurl).json()
sheet_name = os.getenv('sheet_name')


fhc = json_data['data']['result'][0]['value'][1]


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

sheet_select.append_row([date_today, hour_time, fhc])

