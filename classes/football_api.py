#class to call the sports api
import requests
import json
import os
import datetime

class FootballAPI:
    
    def __init__(self):
        #read api key from sports-api.key file
        with open("sports-api.key", "r") as f:
            lines = f.readlines()
            self.api_key = lines[0].strip()
            
        self.url = "https://v3.football.api-sports.io"
        self.headers = {
            'x-rapidapi-key': self.api_key,
            'x-rapidapi-host': self.url
        }
        self.league_id = 39 #EPL
        
        #season is the current year if the month is between July and December. And the previous year if the month is between January and June.
        self.season = datetime.datetime.now().year if datetime.datetime.now().month >= 7 else datetime.datetime.now().year - 1
                
        
    def get_matches_today(self):
        #get todays date in form YYYY-MM-DD
        params = {
            'league': self.league_id,
            'date': datetime.datetime.now().strftime("%Y-%m-%d"),
            # 'date': '2024-08-17', #for testing
            'season': self.season
        }
        print(self.api_key)
        response = requests.get(self.url+'/fixtures', headers=self.headers, params=params)
        print(response.json())
        return response.json()
    
    def get_matches_this_week(self):
        #get todays date in form YYYY-MM-DD
        params = {
            'league': self.league_id,
            'from': datetime.datetime.now().strftime("%Y-%m-%d"),
            'to': (datetime.datetime.now() + datetime.timedelta(days=6)).strftime("%Y-%m-%d"),
            # 'from': '2024-08-19', #for testing
            # 'to': '2024-08-25', #for testing
            'season': self.season
        }
        response = requests.get(self.url+'/fixtures', headers=self.headers, params=params)
        return response.json()
    
    def get_last_ten_matches(self):
        params = {
            'league': self.league_id,
            'last': 10,
            'season': self.season
            # 'season': '2023' #for testing
        }
        response = requests.get(self.url+'/fixtures', headers=self.headers, params=params)
        return response.json()
    
    def get_next_ten_matches(self):
        params = {
            'league': self.league_id,
            'next': 10,
            'season': self.season
        }
        response = requests.get(self.url+'/fixtures', headers=self.headers, params=params)
        return response.json()
    
    def get_standings(self):
        params = {
            'league': self.league_id,
            'season': self.season
        }
        response = requests.get(self.url+'/standings', headers=self.headers, params=params)
        return response.json()

