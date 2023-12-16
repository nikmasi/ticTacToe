import customtkinter

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
        self.var=customtkinter.StringVar(value=self.master.master.player + " turn")
        self.varX = customtkinter.StringVar(value="player X: "+str(self.cntX))
        self.varO = customtkinter.StringVar(value="player O: "+str(self.cntO))

        self.label = customtkinter.CTkLabel(master=self, textvariable=self.var, font=('consolas', 20))
        self.labelX = customtkinter.CTkLabel(master=self, textvariable=self.varX, font=('consolas', 20))
        self.labelO = customtkinter.CTkLabel(master=self, textvariable=self.varO, font=('consolas', 20))

        self.label.pack(side="left", expand=True, pady=10, padx=30)
        self.labelX.pack(side="top",anchor="nw", expand=True, pady=0, padx=30)
        self.labelO.pack(side="top", anchor="nw",expand=True, pady=0, padx=30)

    def change_label_turn(self):
        self.var.set(self.master.master.player+ " turn")

    def change_label_winner(self,string):
        if string=="draw": self.var.set("Tie!")
        else:
            self.var.set(self.master.master.player+ " win")
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
                                               border_width=1,font=('consolas', 12), command=master.master.new_game)
        exit_button = customtkinter.CTkButton(master=self, text="exit", fg_color="black", border_color="white",
                                               border_width=1,font=('consolas', 12), command=master.master.exit_game)

        reset_button.pack(side="top", expand=True, pady=2, padx=5)
        exit_button.pack(side="top", expand=True, pady=2, padx=5)