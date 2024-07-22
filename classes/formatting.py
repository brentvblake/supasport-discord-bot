import datetime
import pytz
import discord
import tabulate

#formatting class
class Formatting:
    
    def __init__(self):
        pass
    
    # Function to format the game data
    def format_game_data_today(self, data):
        games = data['response']
        #get date string eg. Wednesday 2021-08-17
        date_str = datetime.datetime.now().strftime("%A %Y-%m-%d")
        embed = discord.Embed(title=f"{date_str}\nToday's Fixtures", color=0x1e90ff)
        
        for game in games:
            fixture = game['fixture']
            league = game['league']
            home_team = game['teams']['home']
            away_team = game['teams']['away']
            
            # Convert game time to local South African time
            game_time_utc = datetime.datetime.strptime(fixture['date'], '%Y-%m-%dT%H:%M:%S%z')
            game_time_sa = game_time_utc.astimezone(pytz.timezone('Africa/Johannesburg'))
            game_time_str = game_time_sa.strftime('%H:%M')
            
            
            venue = fixture['venue']['name']
            home_team_name = home_team['name']
            away_team_name = away_team['name']
            
            # Add field to the embed for each game
            embed.add_field(name=f"{home_team_name} vs {away_team_name}",
                            value=f"**League:** {league['name']}\n**Time:** {game_time_str} (ZA Time)\n**Venue:** {venue}",
                            inline=False)
            embed.set_thumbnail(url=league['logo'])
        
        return embed
    
    # Function to format the game data
    def format_game_data_week(self, data):
        games = data['response']
        embed = discord.Embed(title="Week's Fixtures", color=0x1e90ff)
        
        for game in games:
            fixture = game['fixture']
            league = game['league']
            home_team = game['teams']['home']
            away_team = game['teams']['away']
            
            # Convert game time to local South African time
            game_time_utc = datetime.datetime.strptime(fixture['date'], '%Y-%m-%dT%H:%M:%S%z')
            # Get the day name in short form
            day_name_short = game_time_utc.strftime('%a')
            game_time_sa = game_time_utc.astimezone(pytz.timezone('Africa/Johannesburg'))
            game_time_str = game_time_sa.strftime('%Y-%m-%d %H:%M')
            
            
            venue = fixture['venue']['name']
            home_team_name = home_team['name']
            away_team_name = away_team['name']
            
            # Add field to the embed for each game
            embed.add_field(name=f"{home_team_name} vs {away_team_name}",
                            value=f"**League:** {league['name']}\n**Date:** {game_time_str} {day_name_short} (ZA Time)\n**Venue:** {venue}",
                            inline=False)
            embed.set_thumbnail(url=league['logo'])
        
        return embed
    
    def format_next_ten_games(self,data):
        games = data['response']
        embed = discord.Embed(title="Next 10 Fixtures", color=0x1e90ff)
        
        for game in games:
            fixture = game['fixture']
            league = game['league']
            home_team = game['teams']['home']
            away_team = game['teams']['away']
            
            # Convert game time to local South African time
            game_time_utc = datetime.datetime.strptime(fixture['date'], '%Y-%m-%dT%H:%M:%S%z')
            game_time_sa = game_time_utc.astimezone(pytz.timezone('Africa/Johannesburg'))
            game_time_str = game_time_sa.strftime('%Y-%m-%d %H:%M')
            
            
            venue = fixture['venue']['name']
            home_team_name = home_team['name']
            away_team_name = away_team['name']
            
            # Add field to the embed for each game
            embed.add_field(name=f"{home_team_name} vs {away_team_name}",
                            value=f"**League:** {league['name']}\n**Date:** {game_time_str} (ZA Time)\n**Venue:** {venue}",
                            inline=False)
            embed.set_thumbnail(url=league['logo'])
        
        return embed
    
     # Function to format the last 10 game data
    def format_last_10_games(self, data):
        games = data['response']
        embed = discord.Embed(title="Last 10 Games Results", color=0x1e90ff)
        
        for game in games:
            fixture = game['fixture']
            home_team = game['teams']['home']
            away_team = game['teams']['away']
            league = game['league']
            
            # Convert game time to local South African time
            game_time_utc = datetime.datetime.strptime(fixture['date'], '%Y-%m-%dT%H:%M:%S%z')
            game_time_sa = game_time_utc.astimezone(pytz.timezone('Africa/Johannesburg'))
            game_time_str = game_time_sa.strftime('%Y-%m-%d %H:%M')
            
            venue = fixture['venue']['name']
            home_team_name = home_team['name']
            away_team_name = away_team['name']

            home_goals = game['goals']['home']
            away_goals = game['goals']['away']
            
            # Add field to the embed for each game
            embed.add_field(
                name=f"{home_team_name} vs {away_team_name}",
                value=(
                    f"{home_team_name} **{home_goals} - {away_goals}** {away_team_name}\n"
                    f"**Date:** {game_time_str} (ZA Time)\n"
                    f"**Venue:** {venue}\n"
                    f"**Status:** {fixture['status']['long']}"
                ),
                inline=False
            )
            embed.set_thumbnail(url=league['logo'])
        return embed
    
    # Function to format the league standings
    def format_league_standings(self, data):
        standings = data['response'][0]['league']['standings'][0]
        league = data['response'][0]['league']
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        embed = discord.Embed(title=f"{league['name']} Standings - {date}", color=0x1e90ff)
        # embed.set_thumbnail(url=league['logo'])
        # Prepare the table data
        table_data = []
        for team in standings:
            rank = team['rank']
            team_name = team['team']['name']
            points = team['points']
            win = team['all']['win']
            draw = team['all']['draw']
            lose = team['all']['lose']
            goal_diff = team['goalsDiff']
            
            table_data.append([rank, team_name, points, f"{win}-{draw}-{lose}", goal_diff])
        
        # Convert table data to a formatted string using tabulate
        table_str = tabulate.tabulate(table_data, headers=["Rank", "Team", "Pts", "W-D-L", "GD"], tablefmt="plain")
        
        # Add the table to the embed
        embed.add_field(name="Standings", value=f"```{table_str}```", inline=False)
        
        return embed