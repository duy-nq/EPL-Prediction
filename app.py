from tkinter import Tk, filedialog, messagebox, PhotoImage, Toplevel
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from support import read_csv, last_5_matches_at, head_to_head
from random import sample, choice

TEAMS_ID = (
    71,
    72,
    73,
    74,
    75,
    76,
    77,
    78,
    79,
    80,
    81,
    82,
    83,
    84,
    85,
    86,
    87,
    88,
    89,
    90,
    91,
    92,
    93,
    219,
    220,
    227,
    228,
    229,
    238,
    245,
    244,
    249,
)
TEAMS = (
    'Aston Villa',
    'Everton',
    'AFC Bournemouth',
    'Southampton',
    'Leicester City',
    'West Bromwich Albion',
    'Sunderland',
    'Crystal Palace',
    'Norwich City',
    'Chelsea',
    'West Ham United',
    'Tottenham Hotspur',
    'Arsenal',
    'Swansea City',
    'Stoke City',
    'Newcastle United',
    'Liverpool',
    'Manchester City',
    'Manchester United',
    'Watford',
    'Hull City',
    'Burnley',
    'Middlesbrough',
    'Huddersfield Town',
    'Brighton and Hove Albion',
    'Cardiff City',
    'Fulham',
    'Wolverhampton Wanderers',
    'Sheffield United',
    'Leeds United',
    'Brentford',
    'Nottingham Forest'
)
SEASON = (
    '1516',
    '1617',
    '1718',
    '1819',
    '1920',
    '2021',
    '2122',
    '2223'
)
class user_interface:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("EPL Prediction")
        self.root.geometry('720x560')
        self.root.resizable(0,0)

        self.model_label = ttk.Label(
            self.root,
            text='1. Prediction model',
            bootstyle=INFO,
            font=('Roboto', 18),
        )
        self.model_label.place(x=10, y=10)

        self.model_entry = ttk.Entry(
            self.root,
            bootstyle=SUCCESS,
            font=('Roboto', 12),
            state='readonly'
        )
        self.model_entry.place(x=40, y=50)

        self.model_btn = ttk.Button(
            self.root, 
            text='Choose a model', 
            bootstyle=SUCCESS,
            command=self.open_file
        )
        self.model_btn.place(x=250, y=53)

        self.teams_label = ttk.Label(
            self.root,
            text='2. Teams',
            bootstyle=INFO,
            font=('Roboto', 18),
        )
        self.teams_label.place(x=10, y=100)   
        
        self.season_label = ttk.Label(
            self.root,
            text='Season: ',
            bootstyle=SECONDARY,
            font=('Roboto', 14),
        )
        self.season_label.place(x=250, y=130)

        self.season = ttk.Combobox(
            self.root,
            bootstyle=DARK,
            font=('Roboto',12),
            state='readonly',
            width=10
        )  
        self.season.place(x=325, y=130)
        self.season['values'] = SEASON
        self.season.bind('<<ComboboxSelected>>', self.handle_season)           

        self.home_team = ttk.Combobox(
            self.root,
            bootstyle=DARK,
            font=('Roboto',12),
            state='readonly'
        )  
        self.home_team.place(x=110, y=300)
        self.home_team.bind('<<ComboboxSelected>>', self.handle_change_1)        

        self.away_team = ttk.Combobox(
            self.root,
            bootstyle=DARK,
            font=('Roboto',13),
            state='readonly'       
        )  
        self.away_team.place(x=400, y=300)
        self.away_team.bind('<<ComboboxSelected>>', self.handle_change_2)

        self.teams_btn = ttk.Button(
            self.root, 
            text='Confirm', 
            bootstyle=SUCCESS,
            command=self.choose_lineup,
            width=20
        )
        self.teams_btn.place(x=287, y=350)

        self.result_label = ttk.Label(
            self.root,
            text='3. Result',
            bootstyle=INFO,
            font=('Roboto', 18),
        )
        self.result_label.place(x=10, y=400)     

        self.logo_1 = PhotoImage(
            file='',
        )
        self.logo_2 = PhotoImage(
            file='',
        )

        self.home_logo = ttk.Label(
            image=self.logo_1
        )
        self.home_logo.place(x=170,y=160)   

        self.away_logo = ttk.Label(
            image=self.logo_2
        )
        self.away_logo.place(x=465,y=160)
        
        self.home_strength_value = 0
        self.away_strength_value = 0     

        self.home_forms = 0
        self.away_forms = 0

        self.head_to_head = 0    

        self.root.mainloop()

    def set_dimension(w: int, h: int, self):
        dim = str(w) + 'x' + str(h)
        self.root.geometry(dim)

    def open_file(self):
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        filename = filedialog.askopenfilename(
            title='Choose a model',
            initialdir='/',
            filetypes=filetypes
        )

        if filename:
            self.model_entry.configure(state='none')
            
            messagebox.showinfo(
                title='Done',
                message='Selected file ' + filename + ' successfully'
            )

            self.model_entry.insert(0, filename[filename.rfind('/')+1:])
            self.model_entry.configure(state='readonly')

    def handle_season(self, event):        
        filename = 'Teams/teams_' + str(self.season.get()) + '.csv'
        data = read_csv(filename)

        teams = ()

        for row in data:
            teams += (row[1],)

        self.home_team['values'] = teams
        self.away_team['values'] = teams

        self.home_team.current(0)
        self.handle_change_1('')
        self.away_team.current(1)
        self.handle_change_2('')

    def handle_change_1(self, event):
        home_id = TEAMS_ID[TEAMS.index(self.home_team.get())]

        self.logo_1.configure(
            file='Logo/' + str(home_id) + '.png'
        )

        self.logo_1 = self.logo_1.subsample(3)

        self.home_logo.configure(
            image=self.logo_1
        )

    def handle_change_2(self, event):
        away_id = TEAMS_ID[TEAMS.index(self.away_team.get())]
            
        self.logo_2.configure(
            file='Logo/' + str(away_id) + '.png'
        )

        self.logo_2 = self.logo_2.subsample(3)

        self.away_logo.configure(
            image=self.logo_2
        )

    def choose_lineup(self):
        try:
            home_id = TEAMS_ID[TEAMS.index(self.home_team.get())]
            away_id = TEAMS_ID[TEAMS.index(self.away_team.get())]

            if home_id == away_id:
                messagebox.showerror(
                title='Warning',
                message='Please choose again!'
                )
                return
            
            self.players_picker = Toplevel()
            self.players_picker.geometry('500x400')
            self.players_picker.title('Team Player')

            self.logo_01 = ttk.Label(
                self.players_picker,
                image=self.logo_1,
            )
            self.logo_01.place(x=10, y=10)

            self.home_name = ttk.Label(
                self.players_picker,
                bootstyle=DANGER,
                font=('Roboto', 14),
                text=self.home_team.get()
            )
            self.home_name.place(x=120, y=15)

            self.home_f1 = ttk.Button(
                self.players_picker,
                bootstyle=(DANGER, OUTLINE),
                text='Formation 1',
                command=self.home_f1_handle
            )
            self.home_f1.place(x=120, y=45)

            self.home_f2 = ttk.Button(
                self.players_picker,
                bootstyle=(DANGER, OUTLINE),
                text='Formation 2',
                command=self.home_f2_handle
            )
            self.home_f2.place(x=120, y=80)

            self.home_strength = ttk.Label(
                self.players_picker,
                bootstyle=SUCCESS,
                font=('Roboto', 30),
                text='NaN'
            )  
            self.home_strength.place(x=350, y=35)

            self.separator_01 = ttk.Separator(
                self.players_picker,
                orient=HORIZONTAL,
                style=DARK,
            )
            self.separator_01.pack(fill='x', pady=130)

            self.logo_02 = ttk.Label(
                self.players_picker,
                image=self.logo_2
            )
            self.logo_02.place(x=10, y=150)

            self.away_name = ttk.Label(
                self.players_picker,
                bootstyle=DARK,
                font=('Roboto', 14),
                text=self.away_team.get()
            )
            self.away_name.place(x=120, y=160)

            self.away_f1 = ttk.Button(
                self.players_picker,
                bootstyle=(DARK, OUTLINE),
                text='Formation 1',
                command=self.away_f1_handle
            )
            self.away_f1.place(x=120, y=190)

            self.away_f2 = ttk.Button(
                self.players_picker,
                bootstyle=(DARK, OUTLINE),
                text='Formation 2',
                command=self.away_f2_handle
            )
            self.away_f2.place(x=120, y=225)

            self.away_strength = ttk.Label(
                self.players_picker,
                bootstyle=SUCCESS,
                font=('Roboto', 30),
                text='NaN'
            )  
            self.away_strength.place(x=350, y=180)

            self.confirm = ttk.Button(
                self.players_picker,
                bootstyle=(DARK, OUTLINE),
                text='START',
                width=30,
                command=self.result,
            )
            self.confirm.place(x=145,y=300)
        except:
            messagebox.showerror(
                title='Warning',
                message='Need to pick two teams!'
            )

    def get_players(self, team: str) -> list[int]:
        filename = 'Players Overall/players_' + str(self.season.get()) + '.csv'

        data = read_csv(filename)

        print(team)

        return [int(row[1]) for row in data if row[2] == team]        

    def ability_100(self, ovr: list[int]) -> float:
        sorted_ovr = sorted(ovr, reverse=True)
        
        return round(sum(sample(sorted_ovr[:14], 11))/11, 2)

    def ability_70(self, ovr: list[int]) -> float:
        sorted_ovr = sorted(ovr, reverse=True)

        return round((sum(sample(sorted_ovr[:15],5)) + sum(sample(sorted_ovr[15:25], 3)) + sum(sample(sorted_ovr[25:], 3)))/11, 2)

    def home_f1_handle(self):
        self.home_strength_value = self.ability_100(self.get_players(self.home_team.get()))
        self.home_strength.configure(
            text=str(self.home_strength_value)
        )

    def home_f2_handle(self):
        self.home_strength_value = self.ability_70(self.get_players(self.home_team.get()))
        self.home_strength.configure(
            text=str(self.home_strength_value)
        )

    def away_f1_handle(self):
        self.away_strength_value = self.ability_100(self.get_players(self.away_team.get()))
        self.away_strength.configure(
            text=str(self.away_strength_value)
        )      

    def away_f2_handle(self):
        self.away_strength_value = self.ability_70(self.get_players(self.away_team.get()))
        self.away_strength.configure(
            text=str(self.away_strength_value)
        )    

    def result(self):
        home_id = TEAMS_ID[TEAMS.index(self.home_team.get())]
        away_id = TEAMS_ID[TEAMS.index(self.away_team.get())]

        r_day = str(choice(range(1,28)))
        if len(r_day) == 1:
            r_day = '0' + r_day

        r_month = str(choice(range(1,12)))
        if len(r_month) == 1:
            r_month = '0' + r_month

        r_year = '20' + choice([str(self.season.get()[:2]), str(self.season.get()[2:])])

        r_date = r_year + '-' + r_month + '-' + r_day
        print(r_date)
        
        self.home_forms = last_5_matches_at(str(home_id), True, r_date)
        self.away_forms = last_5_matches_at(str(away_id), False, r_date)
        self.head_to_head = head_to_head(str(home_id), str(away_id), r_date)

window = user_interface()