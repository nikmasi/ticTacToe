import customtkinter

class FrameBoard(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.frame_rot = customtkinter.CTkFrame(master=self, fg_color="#808080", border_color="#FFFFFF", border_width=0, width=300, height=200)
        self.buttons = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        for row in range(3):
            for column in range(3):
                self.buttons[row][column] = customtkinter.CTkButton(master=self.frame_rot, text="", font=('consolas', 40),fg_color="#D3D3D3",border_color="black",
                                                                    border_width=1,height=80, command=lambda row=row, column=column: self.next_turn(row, column))
                self.buttons[row][column].grid(row=row, column=column,pady=3,padx=2)

        self.frame_rot.pack(side="bottom", anchor="s", pady=5, padx=15)

    def next_turn(self,row, column):
        if(self.buttons[row][column].cget('text')=="" and self.check_winner() is False):
            if(self.master.player=="x"):self.buttons[row][column].configure(text=self.master.player,fg_color="#5F9EA0")
            else:self.buttons[row][column].configure(text=self.master.player,fg_color="#B0C4DE")

            if self.check_winner() is False:
                self.master.change_player()
                self.master.change_label_frame()

            elif self.check_winner() is True:
                self.master.change_label_winner_frame(self.master.player)

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

        if spaces == 0: return False
        else: return True

    def reset_board(self):
        for row in range(3):
            for column in range(3):
                self.buttons[row][column].configure(text="",fg_color="white")
