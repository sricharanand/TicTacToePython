import csv
from datetime import datetime

class HistoryManager:
    def __init__(self, file_name='history.csv'): # by default naming file as history.csv
        self.file_name = file_name

    def get_game_count(self):
        try:
            with open(self.file_name, mode='r') as file: # opening in the read mode
                #  using with as it automatically closes the file after being executed to reduce the errors
                reader = csv.reader(file)
                return sum(1 for _ in reader) # gives us total number of rows
        except FileNotFoundError:
            return 0 # if there are no data in the file
        
    def save_result(self, player1, player2, winner):
        # helps us to write the results of the game
        game_number = self.get_game_count() + 1 # as we are starting from 0, as we also have to print the title of the table we are showing in the ui
        with open(self.file_name, mode='a', newline='') as file: # opening in append mode 
            writer = csv.writer(file) # allowing us to write the csv file 
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # this is the syntax to add year month day hour minute second int the file
            writer.writerow([game_number, now, player1, player2, winner]) # making 

    def load_history(self):
        history = [("Game", "Date and Time", "Player 1", "Player 2", "Winner")]
        # appending this list
        try:
            with open(self.file_name, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    # entering a list
                    history.append((f'{row[0]}', f'{row[1]}', f'{row[2]}', f'{row[3]}', f'{row[4]}'))
        except FileNotFoundError:
            history.append(("No history available.", "", "", "", "")) # when file contains nothing
        return history # returning the appended list


