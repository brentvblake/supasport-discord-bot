#class to call the sports api
import requests
import json
import os
import datetime

class F1API:
    
    def __init__(self):
        #read api key from sports-api.key file
        with open("sports-api.key", "r") as f:
            lines = f.readlines()
            self.api_key = lines[0].strip()
            
        self.url = "https://v1.formula-1.api-sports.io"
        self.headers = {
            'x-rapidapi-key': self.api_key,
            'x-rapidapi-host': self.url
        }
        
        
    def get_players(self):
        response = requests.get(self.url, headers=self.headers)
        return response.json()
    
    def get_player_by_id(self, player_id):
        url = f"{self.url}/{player_id}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_player_by_name(self, name):
        url = f"{self.url}/Search/{name}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_player_by_team(self, team):
        url = f"{self.url}/FreeAgents/{team}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_player_by_position(self, position):
        url = f"{self.url}/FreeAgents/{position}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_player_by_week(self, week):
        url = f"{self.url}/FreeAgents/{week}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_player_by_team_position(self, team, position):
        url = f"{self.url}/FreeAgents/{team}/{position}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_player_by_team_week(self, team, week):
        url = f"{self.url}/FreeAgents/{team}/{week}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_player_by_position_week(self, position, week):
        url = f"{self.url}/FreeAgents/{position}/{week}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_player_by_team_position_week(self, team, position, week):
        url = f"{self.url}/FreeAgents/{team}/{position}/{week}"
        response = requests.get(url, headers=self.headers)
        return response.json()