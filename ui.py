import tkinter as tk
from tkinter import messagebox
from game_logic import TicTacToe
import pygame

#  not creating new windows, just clearing the previous widgets and placing the new ones
class TicTacToeUI:
    def __init__(self, root, history_manager):
        self.root = root
        self.history_manager = history_manager
        self.player1 = "" #initially setting player name 
        self.player2 = ""
        self.tic_tac_toe = None   # object initially
        self.root.title("Tic-Tac-Toe Game")
        self.root.geometry("500x500")
        self.root.config(bg="#835C3B")
        self.root.resizable(False, False)

        # Initialize pygame for background sound
        pygame.mixer.init()

        # Load and play background sound
        pygame.mixer.music.load("bgm.mp3")  #  file exists in your directory
        pygame.mixer.music.play(loops=-1)  # Looping the music 


        self.create_selection_screen()


    def remove_widgets(self):
        for widget in self.root.winfo_children(): 
            # winfo_children is a function which gives info of widgets used
            widget.destroy()

    def create_selection_screen(self):
        self.remove_widgets() # removing all the previous widgets

        title_frame = tk.Frame(self.root, relief="sunken", bd=10, bg="black") # keeping title in a frame as it will look good and give us more freedom in placing it
        title_frame.pack(fill="x") # to make sure that title frame expands horizontally

        title = tk.Label(title_frame, text="TIC-TAC-TOE", font=('Comic Sans MS', 36, 'bold'), bg="#84af1d", fg="#333", padx=140, pady=20)
        title.pack()

        button_frame = tk.Frame(self.root, relief="ridge", bg="black")
        button_frame.pack(pady=120, padx=40, anchor="center")

        #setting up the buttons
        new_game_button = tk.Button(button_frame, text="New Game", command=self.start_new_game,font=('Comic Sans MS', 14), bg="white", fg="black", width=20)
        history_button = tk.Button(button_frame, text="View History", command=self.show_history,font=('Comic Sans MS', 14), bg="white", fg="black", width=20)
        quit_button = tk.Button(button_frame, text="Quit Game", command=self.root.destroy, width=20, font=('Comic Sans MS', 14), bg = 'white')

        # placing the buttons
        new_game_button.grid(row=0,pady=1)
        history_button.grid(row=1,pady=1)
        quit_button.grid(row=2,pady=1)

    def start_new_game(self):
        self.remove_widgets() # removing all the previous widgets

        # now placing new widgets

        title_frame1 = tk.Frame(self.root, relief="sunken", bd=10, bg="black")
        title_frame1.pack()
        tk.Label(title_frame1, text="Enter Player 1 Name", font=('Comic Sans MS', 36, 'bold'), bg="#84af1d", fg="black", width=140, bd=10).pack()
        entry_frame1 = tk.Frame(self.root, relief="sunken", bd=5, bg="black")
        entry_frame1.pack(pady=10)

        # taking information of the player and storing it
    
        player1_name = tk.Entry(entry_frame1, font=('Comic Sans MS', 12), bg="white", fg="black")  # Set bg to white and fg to black
        player1_name.pack()

        title_frame2 = tk.Frame(self.root, relief="sunken", bd=10, bg="black")
        title_frame2.pack()
        tk.Label(title_frame2, text="Enter Player 2 Name", font=('Comic Sans MS', 36, 'bold'), bg="#84af1d", fg="black", width=140, bd=10).pack()
        entry_frame2 = tk.Frame(self.root, relief="sunken", bd=5, bg="black")
        entry_frame2.pack(pady=10)
    
        player2_name = tk.Entry(entry_frame2, font=('Comic Sans MS', 12), bg="white", fg="black")  # Set bg to white and fg to black
        player2_name.pack()

        def start_game():
            self.player1 = player1_name.get() # saving the player name into self.player1 defined in game logic and player2 also
            self.player2 = player2_name.get()
            if self.player1 and self.player2:
                self.tic_tac_toe = TicTacToe(self.player1, self.player2)
                self.create_game_screen()
            else:
                messagebox.showwarning("Input Error", "Both player names must be filled in!")

        button_frame = tk.Frame(self.root, relief="ridge", bg="black", bd=5)
        start_button = tk.Button(button_frame, text="Start Game", command=start_game,
                        font=('Comic Sans MS', 14), bg="white", fg="black", width=20)
        back_button = tk.Button(button_frame, text="Back", command=self.create_selection_screen,
                         font=('Comic Sans MS', 14), bg="white", fg="black", width=20)
        start_button.pack()
        back_button.pack()
        button_frame.pack(pady=10)

    def create_game_screen(self):
        self.remove_widgets()
        # initially starting from X
        self.turn_label = tk.Label(self.root, text=f"{self.player1}'s Turn (X)", font=('Comic Sans MS', 28), bg="#84af1d", fg="#001BFF", width = 140)
        self.turn_label.pack()

        game_frame = tk.Frame(self.root, bd = 5 , relief="sunken", bg = "black")
        game_frame.pack(pady=20)

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        #  creates [[None, None, None],
                    # [None, None, None],
                    # [None, None, None]]

        for i in range(3): # entering a row
            for j in range(3): # entering a column of a row (cell)

                button = tk.Button(game_frame, text="", font=('Comic Sans MS', 30), width=3, height=1,command=lambda r= i , c = j: self.button_click(r, c),bg="#ffffff", activebackground="#cccccc", relief="solid", bd=2)
                # using self.button_click(r,c) which makes x or o value in the respective button

                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = button # making ith row and jth column a button with above specifications

        restart_button = tk.Button(self.root, text="Restart Game", command=self.start_new_game,
                                font=('Comic Sans MS', 12), bg="white", fg="black", width=12)
        restart_button.pack(pady=10)

    def button_click(self, row, col):
        try:
            current_player = self.tic_tac_toe.player  # Capture the current player before making the move, so that game logic and ui shows correct

            self.tic_tac_toe.makemove(row, col)  # Make the move in the game logic and now channing the turn from makemove function
        
            button = self.buttons[row][col]
            button.config(text=current_player, disabledforeground="black",state='disabled', bg="#EEEEEE")
            
            # changing color of font when turn changes
            if current_player == 'X':
                button.config(fg="#4CAF50")  
            else:
                button.config(fg="#2196F3")  
            

        # Check for winner using the function defined in game logic
            if self.tic_tac_toe.is_winner():
                messagebox.showinfo("TIC-TAC-TOE", f"{self.tic_tac_toe.winner} wins!")
                self.history_manager.save_result(self.player1, self.player2, self.tic_tac_toe.winner)
                self.create_selection_screen()  
            elif self.tic_tac_toe.is_draw():
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.history_manager.save_result(self.player1, self.player2, "Draw")
                self.create_selection_screen()
            else:
                self.update_turn()  # Update the turn to the next player in ui

        except ValueError as e:
            messagebox.showwarning("Tic-Tac-Toe", str(e))

    def update_turn(self):
        next_player = self.tic_tac_toe.player 
        if next_player == 'X':
            self.turn_label.config(text=f"{self.player1}'s Turn (X)", fg="#3C44AA")
        else:
            self.turn_label.config(text=f"{self.player2}'s Turn (O)", fg="#B02E26")

    def show_history(self):
        self.remove_widgets()

        title_frame = tk.Frame(self.root, relief="sunken", bd=10, bg="black")
        tk.Label(title_frame, text="Game History", font=('Comic Sans MS', 36, 'bold'), bg="#84af1d", fg="#333", padx=140, pady=20, anchor="n").pack()
        title_frame.pack()

        history_frame = tk.Frame(self.root, bg="black", bd=12, relief="sunken")
        history_frame.pack(pady=10)

        history = self.history_manager.load_history() #using function load history from the file manager file
        
        for i, entry in enumerate(history):
            # for ith index and entry we are making a table with some specifications and using grid to place all info in ith row and respec col.
            # we have used enumerate because i is the index and entry is all the values 
            tk.Label(history_frame, text=entry[0], font=('Comic Sans MS', 15), bg="white", fg="black", bd=2).grid(row=i, column=0, sticky="nsew")
            tk.Label(history_frame, text=entry[1], font=('Comic Sans MS', 15), bg="white", fg="black", bd=2).grid(row=i, column=1, sticky="nsew")
            tk.Label(history_frame, text=entry[2], font=('Comic Sans MS', 15), bg="white", fg="black", bd=2).grid(row=i, column=2, sticky="nsew")
            tk.Label(history_frame, text=entry[3], font=('Comic Sans MS', 15), bg="white", fg="black", bd=2).grid(row=i, column=3, sticky="nsew")
            tk.Label(history_frame, text=entry[4], font=('Comic Sans MS', 15), bg="white", fg="black", bd=2).grid(row=i, column=4, sticky="nsew")
            #  sticky makes label to expand in all the directions n s e w

        button_frame = tk.Frame(self.root, relief="ridge", bg="black", bd=5)
        back_button = tk.Button(button_frame, text="Back", command=self.create_selection_screen,
                         font=('Comic Sans MS', 12), bg="#13B3FE", fg="black", width=12)
        back_button.pack()
        button_frame.pack()
