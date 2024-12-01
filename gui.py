from tkinter import *

class Gui:
    def __init__(self, window):
        self.window = window

        self.frame_one = Frame(self.window)

        self.button_vote = Button(self.frame_one, text='VOTE', command=self.open_candidate_menu) #fix command so that it sends you to candidate menu
        self.button_exit = Button(self.frame_one, text='EXIT', command=self.window.destroy)

        self.button_vote.pack(side='left', padx=5, pady=5)
        self.button_exit.pack(side='left', padx=5, pady=5)
        self.frame_one.pack()



    def open_candidate_menu(self):
        candidate_window = Toplevel(self.window)
        candidate_window.title("CANDIDATE MENU")
        candidate_window.geometry('300x400')

        Button(candidate_window, text="Goku", command=lambda: self.vote(candidate_window, "Candidate 1")).pack(
            pady=5)
        Button(candidate_window, text="Superman", command=lambda: self.vote(candidate_window, "Candidate 2")).pack(
            pady=5)
        Button(candidate_window, text="Peter Griffin", command=lambda: self.vote(candidate_window, "Candidate 3")).pack(
            pady=10)

