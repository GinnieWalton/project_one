from tkinter import *
from tkinter import messagebox
import csv
import os


class Gui:
    def __init__(self, window):
        self.window = window
        self.votes = {"Goku": 0, "Superman": 0, "Peter Griffin": 0}
        self.csv_file = "votes.csv"

        # Ensure the CSV file exists and initialize it if needed
        self.initialize_csv()

        # Main Vote Menu
        self.frame_one = Frame(self.window, bg='lightblue')
        self.frame_one.pack(fill='both', expand=True)
        Label(self.frame_one, text="Vote Menu", font=("Arial", 16), bg='lightblue').pack(pady=10)

        self.button_vote = Button(self.frame_one, text='VOTE', command=self.open_candidate_menu)
        self.button_exit = Button(self.frame_one, text='EXIT', command=self.window.destroy)


        self.button_vote.pack(pady=5)
        self.button_exit.pack(pady=5)
        self.frame_one.pack()

    def initialize_csv(self):
        """Create the CSV file if it doesn't exist and initialize it with candidates."""
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Candidate", "Votes"])  # Add headers
                for candidate in self.votes:
                    writer.writerow([candidate, 0])

    def read_votes_from_csv(self):
        """Load votes from the CSV file."""
        if os.path.exists(self.csv_file):
            with open(self.csv_file, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip headers
                for row in reader:
                    self.votes[row[0]] = int(row[1])

    def write_votes_to_csv(self):
        """Update the CSV file with the current vote counts."""
        with open(self.csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Candidate", "Votes"])  # Add headers
            for candidate, count in self.votes.items():
                writer.writerow([candidate, count])

    def open_candidate_menu(self):
        """Display the candidate menu."""
        candidate_window = Toplevel(self.window)
        candidate_window.title("CANDIDATE MENU")
        candidate_window.geometry('300x200')
        candidate_window.config(bg='lightblue')

        Label(candidate_window, text="Candidate Menu", font=("Arial", 14), bg='lightblue').pack(pady=10)

        # Buttons for voting
        Button(candidate_window, text="Goku", command=lambda: self.vote(candidate_window, "Goku")).pack(pady=5)
        Button(candidate_window, text="Superman", command=lambda: self.vote(candidate_window, "Superman")).pack(pady=5)
        Button(candidate_window, text="Peter Griffin", command=lambda: self.vote(candidate_window, "Peter Griffin")).pack(pady=5)

    def vote(self, window, candidate):
        """Register a vote for the selected candidate."""
        # Increment vote count
        self.votes[candidate] += 1

        # Update the CSV file
        self.write_votes_to_csv()

        # Show confirmation
        messagebox.showinfo("Vote Registered", f"You voted for {candidate}.")
        window.destroy()

        # Optionally, display updated results
        self.display_results()

    def display_results(self):
        """Show the current vote tallies."""
        results_window = Toplevel(self.window)
        results_window.title("Results")
        results_window.geometry('300x200')
        results_window.config(bg='lightblue')

        Label(results_window, text="Current Vote Results", font=("Arial", 14), bg='lightblue').pack(pady=10)

        # Display vote counts
        for candidate, vote_count in self.votes.items():
            Label(results_window, text=f"{candidate}: {vote_count} votes", bg='lightblue').pack()
