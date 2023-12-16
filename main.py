import customtkinter
import random

from frame import FrameLeft,FrameRight,Frame
from frameBoard import FrameBoard

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x400")
        self.title("tic tac toe")
        customtkinter.set_appearance_mode("dark")
        self.resizable(False,False)

        self.players = ["x", "o"]
        self.player = random.choice(self.players)
        self.buttons = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

        self.frame=Frame(self)
        self.frame.pack(side="top", anchor="nw", padx=10, pady=10)

        self.frameBoard = FrameBoard(self)
        self.frameBoard.pack(side="top", padx=10, pady=10)

    def change_label_frame(self):
        self.frame.frame1.change_label_turn()
    def change_label_winner_frame(self,string):
        self.frame.frame1.change_label_winner(string)
    def reset_table(self):
        self.frameBoard.reset_board()

    def exit_game(self):
        app.quit()

    def new_game(self):
        self.player = random.choice(self.players)
        self.change_player()
        app.change_label_frame()
        app.reset_table()

    def change_player(self):
        if (self.player == "x"):
            self.player = "o"
        else:
            self.player = "x"

if __name__ == "__main__":
    app = App()
    app.mainloop()