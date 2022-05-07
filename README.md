# Movie-Picker-For-Google-Sheets-In-Python
Python code for picking a random movie from your list, completely psuedo-random.

##This code was created by Logan Maupin aka Voltaic314 on Github. I am a student at the University of Arizona Online studying Applied Computing - Artificial Intelligence. It is my hope that one day with my degree (once I graduate) I will be able to contribute to research and application projects of Machine Learning in Natural Language Processing. I believe it is the future of General AI Intelligence and will be the forefront to the new AI revolution. Exciting times are ahead, I am just one lowly programmer nerd contributing his works one project at a time. 


############


To put it simply, the way this code works is by creating a developer google account, and then allowing a bot account to read your spreadsheets (which the bot is just this script, the bot account is just a way for the script to login and access the google api). So you create a google sheets developer bot account, get an API token and store it somewhere. It will be a json file, which is what the "keys" part of the code is. You'll also need to grab the spreadsheet ID of your specific sheet that you're looking to read from. This is specific to yours so that's why it's not included directly in this code. To get your ID, it should be in the URL of your specific sheet when you access it. Anyways once you have those 2 things, (for which the sheet ID will need to be modified into the code), then you can run this on your movie list spreadsheets. 


############


The way the code picks a movie is very specific. You will need to add a watched column into your spreadsheet somewhere, doesn't matter where just as long as it is on the same row as each movie. What the code is looking for is specifically *No*  -- if it doesn't see that somewhere in the column it will NOT pick a movie. This is because in my specific list of movies we want to keep movies on the list even after we've watched them, so we can give them a rating and share thoughts about it on the spreadsheet. Like a portfolio. If you don't want to do all this like we did, all you have to do is delete the strmatch parts of the code, then it will just pick any item on the sheet at random given whatever range of values you gave it. 

Note that this code treats every single row in the spreadsheet as a single item, well it's actually a tuple I believe, a list of lists. It puts every element of the row into a list, then puts all those lists into a master list of movies. The "str match" part is pruning that list to only include unwatched movies. But as mentioned before you can modify that. 

Final thoughts: I also at one point thought about modifying this code so that you can filter by genre based on user input like genre_input = input("What genre(s) would you like to watch today?") where the final line of code has some kind of if any(x for x in str_match) blah blah way to filter that in. If you want to see what I mean check out my Wordle Seeker project for how to do this. But anyways I just never got around to it, got caught up in better projects and personally I kind of like the completely random nature of the predictions. I always thought filtering would kind of defeat the purpose of drawing movies out of a virtual hat so-to-speak. Anyways enjoy. Feel free to suggest contributions to improve the code! 
