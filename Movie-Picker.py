from googleapiclient.discovery import build
from google.oauth2 import service_account
import random
import config

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None #writes this variable to no value before overwriting it with the info we need, basically cleaning and prepping it
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES) #writes the creds value with the value from the keys json file above

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=config.config_stuff['SAMPLE_SPREADSHEET_ID'],
                            range="Media!A1:F999").execute()

values = result.get('values', []) #get values from spreadsheet

str_match = [s for s in values if "*No*" in s] #creates a variable for all the lines of the spreadsheet that contain *No*

print("Media Title, Genre, Watched by Nyx? & Watched by Logan? - Nyx's Rating - Logan's Rating") #This prints this line into text to make the output easier to understand
print(random.choice(str_match)) #This prints a single random output from all the values that match the str_match criteria