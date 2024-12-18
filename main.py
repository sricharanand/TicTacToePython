from game_logic import TicTacToe
from ui import TicTacToeUI
from file_manager import HistoryManager
import tkinter as tk

def main():
    root = tk.Tk()
    history_manager = HistoryManager('history.csv') # naming the csv file name
    app = TicTacToeUI(root, history_manager)
    root.mainloop()

if __name__ == "__main__":
    main()