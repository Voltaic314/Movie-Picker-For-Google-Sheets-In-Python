from googleapiclient.discovery import build
from google.oauth2 import service_account
import random
import config #import config is only necessary for the spreadsheet ID variable that I was hiding in my code. If you inject your ID directly into your code you can do away with this line. 

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None #writes this variable to no value before overwriting it with the info we need, basically cleaning and prepping it
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES) #writes the creds value with the value from the keys json file above

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=config.config_stuff['SAMPLE_SPREADSHEET_ID'],
                            range="Media!A1:F999").execute() # Please note that the "Media!" part of this denotes the name of the sheet itself on the overall spreadsheet, make sure yours matches otherwise the code will not work. 
# also note above that the A1:F999 represents the range. The code treats every row as a single list, so best to organize your media row by row as a single item. Your range can be whatever you need. 

values = result.get('values', []) #get values from spreadsheet

str_match = [s for s in values if "*No*" in s] #creates a variable for all the lines of the spreadsheet that contain *No*

#Note that each item in the following line represents a column in the spreadsheet we used, feel free to modify this line however to fit your needs, this has nothing to do with the actual spreadsheet, mainly just printing a line to understand what you are reading). 
print("Media Title, Genre, Watched by Person A? & Watched by Person B? - Person A's Rating - Person B's Rating") #This prints this line into text to make the output easier to understand

#This prints a single random output from all the values that match the str_match criteria
print(random.choice(str_match)) 
