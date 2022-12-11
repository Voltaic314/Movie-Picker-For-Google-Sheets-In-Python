from googleapiclient.discovery import build  # used for Google sheets info
from google.oauth2 import service_account  # also used for Google sheets info
import tkinter as tk
import random


def set_up_sheets():
    """
    This function's purpose is to read the spreadsheet data with the given credentials and return the sheets service
    so we can use it in other functions below.
    :returns: sheet service object that we can use in other function calls for manipulating the spreadsheets.
    """
    SERVICE_ACCOUNT_FILE = 'keys.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None  # writes this variable to no value before overwriting it with the info we need, basically cleaning and prepping it
    # noinspection PyRedeclaration
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)  # writes the creds value with the value from the keys json file above

    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()

    return sheet


def get_movie_list(sheet: object, watched: bool):

    if watched:
        # grab the sheet info from the API
        result_w = sheet.values().get(spreadsheetId=config.config_stuff['SAMPLE_SPREADSHEET_ID'],
                                      range="Movies!I:L").execute()

        # build that into a list of lists
        watched_movies = result_w.get('values', [])
        watched_movies -= watched_movies[0]
        return watched_movies

    else:
        # grab the sheet info from the API
        result_u = sheet.values().get(spreadsheetId=config.config_stuff['SAMPLE_SPREADSHEET_ID'],
                                      range="Movies!A:F").execute()

        # build that into a list of lists
        unwatched_movies = result_u.get('values', [])
        unwatched_movies -= unwatched_movies[0]
        return unwatched_movies


# Create the main window
window = tk.Tk()
window.geometry("400x200")
window.title("Movie Picker")


# Define a function to pick a random movie from the list
def pick_movie(seen: bool):
    # Filter the list of movies based on whether the user has seen them before
    if seen:
        choices = get_movie_list(sheet=set_up_sheets(), watched=True)
    else:
        choices = get_movie_list(sheet=set_up_sheets(), watched=False)

    # Pick a random movie from the list
    choice = random.choice(choices)

    # Display the chosen movie on the screen
    movie_label.config(text=choice)


# Create a label to display the chosen movie
movie_label = tk.Label(window, text="")
movie_label.pack()

# Create a button to pick a random movie from the list of movies the user has not seen
pick_button = tk.Button(window, text="Pick a movie I haven't seen", command=lambda: pick_movie(seen=False))
pick_button.pack()

# Create a button to pick a random movie from the list of movies the user has seen
seen_button = tk.Button(window, text="Pick a movie I have seen", command=lambda: pick_movie(seen=True))
seen_button.pack()

# Display the main window
window.mainloop()
