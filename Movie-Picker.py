from googleapiclient.discovery import build #used for google sheets info
from google.oauth2 import service_account # also used for google sheets info
import random #used for generating random choice (duh)
import config #used to hold our sensitive info
import time #used for sleep (lol)

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None #writes this variable to no value before overwriting it with the info we need, basically cleaning and prepping it
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES) #writes the creds value with the value from the keys json file above

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()

watched_or_unwatched_prompt = str(input("Would you like to watch a new random movie today or a random movie you have already watched? \nPlease type: W for watched or U for unwatched:\n(at any time type X to exit the program)\n")).upper()

result_headers_w = sheet.values().get(spreadsheetId=config.config_stuff['SAMPLE_SPREADSHEET_ID'],
                            range="Movies!I2:N2").execute()

column_headers_w = result_headers_w.get('values', []) #get values from spreadsheet

result_headers_u = sheet.values().get(spreadsheetId=config.config_stuff['SAMPLE_SPREADSHEET_ID'],
                            range="Movies!A2:F2").execute()

column_headers_u = result_headers_u.get('values', []) #get values from spreadsheet

running = True
while running:
    if watched_or_unwatched_prompt == "W":

        #grab the sheet info from the API
        result_w = sheet.values().get(spreadsheetId=config.config_stuff['SAMPLE_SPREADSHEET_ID'],
                                    range="Movies!I:N").execute()

        # build that into a list of lists
        watched_movies = result_w.get('values', [])

        #make the program seem more retro and realistic
        print("Generating random watched movie, please wait...\n")

        #sleeps make people think the program works better believe it or not. lol
        time.sleep(3)
        print(column_headers_w) # This prints this line into text to make the output easier to understand
        print(random.choice(watched_movies)) # This prints a single random output from all the values in the watched columns.

        # determine whether user is satisfied with the randomly generated selection
        satisfied_input_w = str(input("\nAre you satisfied with this result?\nPlease enter Y or N:\n(At any time type X to exit the program)\n")).upper()

        #if statements to determine whether the code should run agian or not. (Note that continue here will only generate a movie in the U or W category, whichever was selected at the start.
        if satisfied_input_w == "Y":
            running = False
        elif satisfied_input_w == "N":
            continue
        elif satisfied_input_w == "X":
            running = False
        else:
            print("I didn't quite catch that. Would you like to watch a movie you've seen before or a new movie? Please entier W or U:\n")

    elif watched_or_unwatched_prompt == "U":

        #grab the sheet info from the API
        result_u= sheet.values().get(spreadsheetId=config.config_stuff['SAMPLE_SPREADSHEET_ID'],
                                    range="Movies!A:F").execute()

        #build that into a list of lists
        unwatched_movies = result_u.get('values', [])

        #make the program seem more retro and realistic
        print("Generating random unwatched movie, please wait...\n")

        #sleeps make people think the program works better, believe it or not. lol
        time.sleep(3)
        print(column_headers_u)# This prints this line into text to make the output easier to understand
        print(random.choice(unwatched_movies))  # This prints a single random output from all the values in the unwatched columns

        # determine whether user is satisfied with the randomly generated selection
        satisfied_input_u = str(input("\nAre you satisfied with this result?\nPlease enter Y or N:\n(At any time type X to exit the program)\n")).upper()

        #if statements to determine whether the code should run agian or not. (Note that continue here will only generate a movie in the U or W category, whichever was selected at the start.
        if satisfied_input_u == "Y":
            running = False
        elif satisfied_input_u == "N":
            continue
        elif satisfied_input_u == "X":
            running = False
        else:
            print("I didn't quite catch that. Would you like to watch a movie you've seen before or a new movie? Please entier W or U:\n")

    #finish the program / break the loop.
    elif watched_or_unwatched_prompt == "X":
        running = False

    # tell the user they are a moron for not inputting the one of only 2 options they had available to them.
    else:
        print("I didn't quite catch that. Would you like to watch a movie you've seen before or a new movie? Please entier W or U:\n")
        continue

#just so the user knows for sure...
print("Program finished.")
