import customtkinter
import random

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x400")
        self.title("tic tac toe")
        customtkinter.set_appearance_mode("dark")
        self.resizable(False,False)

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


def new_game():
    global player

    player = random.choice(players)

    change_player()

    global app
    app.change_label_frame()
    app.reset_table()

players = ["x", "o"]
player = random.choice(players)
buttons = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

def change_player():
    global player
    if(player=="x"): player="o"
    else: player="x"
    return player


class Frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.frame_rot = customtkinter.CTkFrame(master=master, fg_color="#8D6F3A", border_color="#FFCC70",
                                                border_width=2, width=400, height=400)
        self.frame1 = FrameLeft(self)
        self.frame2 = FrameRight(self)

        self.frame1.pack(side="left", anchor="nw", padx=10, pady=10)
        self.frame2.pack(side="right",anchor="ne",padx=10,pady=10)

class FrameLeft(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.frame_rot = customtkinter.CTkFrame(master=master, fg_color="#8D6F3A",border_color="#FFCC70",border_width=2,width=400,height=400)
        self.cntX = 0
        self.cntO = 0
        self.var=customtkinter.StringVar(value=player + " turn")
        self.varX = customtkinter.StringVar(value="player X: "+str(self.cntX))
        self.varO = customtkinter.StringVar(value="player O: "+str(self.cntO))


        self.label = customtkinter.CTkLabel(master=self, textvariable=self.var, font=('consolas', 20))
        self.labelX = customtkinter.CTkLabel(master=self, textvariable=self.varX, font=('consolas', 20))
        self.labelO = customtkinter.CTkLabel(master=self, textvariable=self.varO, font=('consolas', 20))

        self.label.pack(side="left", expand=True, pady=10, padx=30)
        self.labelX.pack(side="top",anchor="nw", expand=True, pady=0, padx=30)
        self.labelO.pack(side="top", anchor="nw",expand=True, pady=0, padx=30)

    def change_label_turn(self):
        self.var.set(player+ " turn")

    def change_label_winner(self,string):
        if string=="draw": self.var.set("Tie!")
        else:
            self.var.set(player+ " win")
            if(string=="x"):
                self.cntX=self.cntX+1
                self.varX.set("player X: "+str(self.cntX))
            else:
                self.cntO = self.cntO + 1
                self.varO.set("player O: " + str(self.cntO))


class FrameRight(customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.frame_rot = customtkinter.CTkFrame(master=master, fg_color="#8D6F3A",border_color="#FFCC70",border_width=2,width=300,height=400)

        reset_button = customtkinter.CTkButton(master=self, text="restart", fg_color="black", border_color="white",
                                               border_width=1,font=('consolas', 12), command=new_game)
        exit_button = customtkinter.CTkButton(master=self, text="exit", fg_color="black", border_color="white",
                                               border_width=1,font=('consolas', 12), command=self.exit_game)

        reset_button.pack(side="top", expand=True, pady=2, padx=5)
        exit_button.pack(side="top", expand=True, pady=2, padx=5)

    def exit_game(self):
        global app
        app.quit()

class FrameBoard(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.frame_rot = customtkinter.CTkFrame(master=self, fg_color="#808080", border_color="#FFFFFF", border_width=0, width=300, height=200)
        self.buttons = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        for row in range(3):
            for column in range(3):
                self.buttons[row][column] = customtkinter.CTkButton(master=self.frame_rot, text="", font=('consolas', 40),fg_color="#D3D3D3",border_color="black",
                                                                    border_width=1,height=80,
                                                               command=lambda row=row, column=column: self.next_turn(row, column))
                self.buttons[row][column].grid(row=row, column=column,pady=3,padx=2)

        self.frame_rot.pack(side="bottom", anchor="s", pady=5, padx=15)

    def next_turn(self,row, column):

        global player
        global players

        if(self.buttons[row][column].cget('text')=="" and self.check_winner() is False):
            if(player=="x"):self.buttons[row][column].configure(text=player,fg_color="#5F9EA0")
            else:self.buttons[row][column].configure(text=player,fg_color="#B0C4DE")


            if self.check_winner() is False:
                change_player()
                self.master.change_label_frame()

            elif self.check_winner() is True:
                self.master.change_label_winner_frame(player)

            elif self.check_winner() == "Tie":
                self.master.change_label_winner_frame("draw")

    def check_winner(self):

        for row in range(3):
            if self.buttons[row][0].cget('text') == self.buttons[row][1].cget('text') == self.buttons[row][2].cget('text') != "":
                self.buttons[row][0].configure(bg_color="green")
                self.buttons[row][1].configure(bg_color="green")
                self.buttons[row][2].configure(bg_color="green")
                return True

        for column in range(3):
            if self.buttons[0][column].cget('text') == self.buttons[1][column].cget('text') == self.buttons[2][column].cget('text') != "":
                self.buttons[0][column].configure(bg_color="green")
                self.buttons[1][column].configure(bg_color="green")
                self.buttons[2][column].configure(bg_color="green")
                return True

        if self.buttons[0][0].cget('text') == self.buttons[1][1].cget('text') == self.buttons[2][2].cget('text') != "":
            self.buttons[0][0].configure(bg_color="green")
            self.buttons[1][1].configure(bg_color="green")
            self.buttons[2][2].configure(bg_color="green")
            return True

        elif self.buttons[0][2].cget('text') == self.buttons[1][1].cget('text') == self.buttons[2][0].cget('text') != "":
            self.buttons[0][2].configure(bg_color="green")
            self.buttons[1][1].configure(bg_color="green")
            self.buttons[2][0].configure(bg_color="green")
            return True

        elif self.empty_spaces() is False:

            for row in range(3):
                for column in range(3):
                    self.buttons[row][column].configure(bg_color="yellow")
            return "Tie"

        else:
            return False

    def empty_spaces(self):

        spaces = 9

        for row in range(3):
            for column in range(3):
                if self.buttons[row][column].cget('text')!="":
                    spaces -= 1

        if spaces == 0:
            return False
        else:
            return True

    def reset_board(self):
        for row in range(3):
            for column in range(3):
                self.buttons[row][column].configure(text="",fg_color="white")


if __name__ == "__main__":
    app = App()
    app.mainloop()