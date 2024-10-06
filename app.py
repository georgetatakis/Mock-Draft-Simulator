from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)



#This class defines the attributes for each prospect.
class Prospect:
    #Initializes each attribute. 
   def __init__(self, name, position, college, weight, height, average_position_rank, average_overall_rank,rating,team_rating=0):
       self.name = name
       self.position = position
       self.college = college
       self.weight = weight
       self.height = height
       self.average_position_rank = average_position_rank
       self.average_overall_rank = average_overall_rank
       self.rating = rating
       self.team_rating=team_rating
   def __str__(self):
       return f"Prospect(name='{self.name}',position='{self.position}',college='{self.college}',weight='{self.weight}',height={self.height}',average_position_rank={self.average_position_rank}',average_overall_rank={self.average_overall_rank}',rating={self.rating}',team_rating={self.team_rating})"

#List of all the positions in the draft.
positions= ["Quarterback","Running Back","Wide Receiver","Tight End","Offensive Tackle","Offensive Guard","Center","Defensive Tackle","Edge","Linebacker","Cornerback","Safety"]

#List of all the prospects.
prospect_list = [
   Prospect("Caleb Williams", "Quarterback", "USC", 214, "6-1", 1, 2.4, 93.6),
   Prospect("Marvin Harrison Jr.", "Wide Receiver", "Ohio State", 209, "6-3", 1, 1.8, 93.6),
   Prospect("Malik Nabers", "Wide Receiver", "LSU", 200, "6-0", 2, 6.2, 92.8),
   Prospect("Joe Alt", "Offensive Tackle", "Notre Dame", 321, "6-9", 1, 6.6, 92.0),
   Prospect("Brock Bowers", "Tight End", "Georgia", 243, "6-3", 1, 6.5, 91.1),
   Prospect("Jayden Daniels", "Quarterback", "LSU", 210, "6-4", 3, 16, 90.9),
   Prospect("Drake Maye", "Quarterback", "North Carolina", 223, "6-4", 2, 5.6, 90.9),
   Prospect("Olumuyiwa Fashanu", "Offensive Tackle", "Penn State", 312, "6-6", 2, 10.8, 89.9),
   Prospect("Michael Penix Jr.", "Quarterback", "Washington", 216, "6-2", 5, 42.7, 89.8),
   Prospect("Rome Odunze", "Wide Receiver", "Washington", 212, "6-3", 3, 8.6, 90.2),
   Prospect("Laiatu Latu", "Edge", "UCLA", 259, "6-5", 2, 14.2, 89.8),
   Prospect("Jared Verse", "Edge", "Florida State", 254, "6-4", 1, 13.2, 89.5),
   Prospect("Jer'Zhan Newton", "Defensive Tackle", "Illinois", 304, "6-2", 3, 18.5, 86.5),
   Prospect("Dallas Turner", "Edge", "Alabama", 247, "6-3", 1, 12.1, 89.3),
   Prospect("JC Latham", "Offensive Tackle", "Alabama", 342, "6-6", 3, 16.7, 89.0),
   Prospect("Quinyon Mitchell", "Cornerback", "Toledo", 195, "6-0", 1, 17.6, 88.8),
   Prospect("Taliese Fuaga", "Offensive Tackle", "Oregon State", 324, "6-6", 4, 19.5, 88.7),
   Prospect("Troy Fautanu", "Offensive Tackle", "Washington", 317, "6-4", 5, 19.8, 88.6),
   Prospect("Byron Murphy II", "Defensive Tackle", "Texas", 297, "6-0", 4, 21.3, 89.6),
   Prospect("Terrion Arnold", "Cornerback", "Alabama", 189, "6-0", 4, 22.9, 88.4),
   Prospect("Cooper DeJean", "Cornerback", "Iowa", 203, "6-0", 2, 22.2, 88.3),
   Prospect("Brian Thomas Jr.", "Wide Receiver", "LSU", 209, "6-3", 4, 23.6, 88.0),
   Prospect("Amarius Mims", "Offensive Tackle", "Georgia", 340, "6-8", 6, 22, 87.9),
   Prospect("Chop Robinson", "Edge", "Penn State", 254, "6-3", 5, 23.7, 87.9),
   Prospect("Graham Barton", "Offensive Guard", "Duke", 313, "6-5", 7, 29.2, 87.9),
   Prospect("Nate Wiggins", "Cornerback", "Clemson", 173, "6-1", 3, 22.8, 86.8),
   Prospect("J.J. McCarthy", "Quarterback", "Michigan", 219, "6-2", 4, 31.8, 86.7),
   Prospect("Kool-Aid McKinstry", "Cornerback", "Alabama", 199, "6-0", 5, 24.7, 86.6),
   Prospect("Ladd McConkey", "Wide Receiver", "Georgia", 186, "6-0", 8, 38.1, 86.6),
   Prospect("Jackson Powers-Johnson", "Center", "Oregon", 328, "6-3", 8, 30.3, 87.4),
   Prospect("Tyler Guyton", "Offensive Tackle", "Oklahoma", 322, "6-8", 9, 33.3, 87.4),
   Prospect("Adonai Mitchell", "Wide Receiver", "Texas", 205, "6-2", 7, 34.7, 87.4),
   Prospect("Bo Nix", "Quarterback", "Oregon", 214, "6-2", 6, 45.2, 87.4),
   Prospect("Jordan Morgan", "Offensive Tackle", "Arizona", 311, "6-5", 10, 39.5, 87.2),
   Prospect("Troy Franklin", "Wide Receiver", "Oregon", 176, "6-2", 10, 45.2, 85.2),
   Prospect("Darius Robinson", "Defensive Tackle", "Missouri", 285, "6-5", 7, 40.8, 87.9),
   Prospect("Ennis Rakestraw Jr.", "Cornerback", "Missouri", 183, "5-11", 8, 43.9, 86.9),
   Prospect("Braden Fiske", "Defensive Tackle", "Florida State", 292, "6-4", 10, 51.4, 86.9),
   Prospect("Payton Wilson", "Linebacker", "North Carolina State", 233, "6-4", 6, 54.7, 86.9),
   Prospect("Tyler Nubin", "Safety", "Minnesota", 199, "6-1", 9, 45.2, 86.8),
   Prospect("Ja'Tavion Sanders", "Tight End", "Texas", 245, "6-4", 3, 57, 86.8),
   Prospect("Roman Wilson", "Wide Receiver", "Michigan", 185, "5-11", 12, 54.5, 86.6),
   Prospect("Ricky Pearsall", "Wide Receiver", "Florida", 189, "6-1", 15, 57.3, 87.7),
   Prospect("Jonathon Brooks", "Running Back", "Texas", 216, "6-0", 4, 67.3, 86.7),
   Prospect("Keon Coleman", "Wide Receiver", "Florida State", 213, "6-3", 6, 32.7, 87.5),
   Prospect("Junior Colson", "Linebacker", "Michigan", 238, "6-2", 7, 59.9, 86.39),
   Prospect("Xavier Worthy", "Wide Receiver", "Texas", 165, "5-11", 9, 40, 86.4),
   Prospect("Edgerrin Cooper", "Linebacker", "Texas A&M", 230, "6-2", 4, 49.8, 86.3),
   Prospect("Kris Jenkins", "Defensive Tackle", "Michigan", 299, "6-3", 11, 53.4, 86.23),
   Prospect("Malachi Corley", "Wide Receiver", "Western Kentucky", 215, "5-11", 18, 66.1, 86.2),
   Prospect("Mike Sainristil", "Cornerback", "Michigan", 182, "5-9", 15, 63.8, 86.1),
   Prospect("Chris Braswell", "Edge", "Alabama", 251, "6-3", 5, 54.6, 86.0),
   Prospect("Xavier Legette", "Wide Receiver", "South Carolina", 221, "6-1", 13, 54.7, 88.0),
   Prospect("Javon Bullard", "Safety", "Georgia", 198, "5-10", 13, 57.8, 86.0),
   Prospect("Christian Haynes", "Offensive Guard", "Connecticut", 317, "6-3", 16, 64.8, 85.9),
   Prospect("Adisa Isaac", "Edge", "Penn State", 247, "6-4", 19, 68.9, 85.9),
   Prospect("Zach Frazier", "Center", "West Virginia", 313, "6-3", 13, 54.9, 85.8),
   Prospect("T.J. Tampa", "Cornerback", "Iowa State", 189, "6-1", 14, 58.5, 85.8),
   Prospect("Jaylen Wright", "Running Back", "Tennessee", 210, "5-10", 6, 74, 85.8),
   Prospect("Kamari Lassiter", "Cornerback", "Georgia", 186, "6-0", 10, 46.3, 85.6)
]




#Dictionary that shows at what pick each team drafts at.  
draft_order = {
   1: "Bears",
   2: "Commanders",
   3: "Patriots",
   4: "Cardinals",
   5: "Chargers",
   6: "Giants",
   7: "Titans",
   8: "Falcons",
   9: "Bears",
   10: "Jets",
   11: "Vikings",
   12: "Broncos",
   13: "Raiders",
   14: "Saints",
   15: "Colts",
   16: "Seahawks",
   17: "Jaguars",
   18: "Bengals",
   19: "Rams",
   20: "Steelers",
   21: "Dolphins",
   22: "Eagles",
   23: "Vikings",
   24: "Cowboys",
   25: "Packers",
   26: "Buccaneers",
   27: "Cardinals",
   28: "Bills",
   29: "Lions",
   30: "Ravens",
   31: "49ers",
   32: "Chiefs"
}


class Team:
    #Intializes the team class.
   def __init__(self,team_name,first_need,second_need):
       self.team_name=team_name
       self.first_need=first_need
       self.second_need=second_need
  
   def __str__(self):
       return f"Team(team_name='{self.team_name}',firstNeed='{self.first_need}',second_need='{self.second_need}')"
#List of NFL teams and each of their needs.
NFL_teams=[
   Team("Bears", "Quarterback", "Edge"),
   Team("Commanders", "Quarterback", "Cornerback"),
   Team("Patriots", "Quarterback", "Offensive Tackle"),
   Team("Cardinals", "Wide Receiver", "Cornerback"),
   Team("Chargers", "Offensive Tackle", "Linebacker"),
   Team("Giants", "Wide Receiver", "Offensive Tackle"),
   Team("Titans", "Wide Receiver", "Offensive Tackle"),
   Team("Falcons", "Defensive Tackle", "Cornerback"),
   Team("Jets", "Offensive Tackle", "Tight End"),
   Team("Vikings", "Quarterback", "Cornerback"),
   Team("Broncos", "Quarterback", "Linebacker"),
   Team("Raiders","Cornerback","Linebacker"),
   Team("Saints", "Offensive Tackle", "Linebacker"),
   Team("Colts", "Quarterback", "Offensive Tackle"),
   Team("Seahawks", "Defensive Tackle", "Linebacker"),
   Team("Jaguars", "Defensive Tackle", "Wide Receiver"),
   Team("Bengals", "Cornerback", "Offensive Guard"),
   Team("Rams", "Offensive Tackle", "Edge"),
   Team("Steelers", "Offensive Tackle", "Cornerback"),
   Team("Dolphins", "Offensive Tackle", "Center"),
   Team("Eagles", "Linebacker", "Cornerback"),
   Team("Cowboys", "Offensive Tackle", "Wide Receiver"),
   Team("Packers", "Offensive Tackle", "Linebacker"),
   Team("Buccaneers", "Offensive Guard", "Offensive Tackle"),
   Team("Bills", "Wide Receiver", "Safety"),
   Team("Lions", "Cornerback", "Edge"),
   Team("Ravens", "Wide Receiver", "Cornerback"),
   Team("49ers", "Offensive Tackle", "Cornerback"),
   Team("Chiefs", "Wide Receiver", "Cornerback")
]
#Creates a dictionary that maps teams to their team needs.
teams_draft_order = {team.team_name: team for team in NFL_teams}

#Holds the user's team choice.
selected_team = None

#Stores each team's draft as the code runs.
draft_summary = []  

#Sort function used for sorting prospect when user is drafting.
def bubble_sort(arr, key):
   n = len(arr)
   for i in range(n):
       for j in range(0, n - i - 1):
           if getattr(arr[j], key) < getattr(arr[j + 1], key):
               arr[j], arr[j + 1] = arr[j + 1], arr[j]

#Routes the user to the first page where the user selects their team.
@app.route('/', methods=['GET', 'POST'])
def index():
   global selected_team
   if request.method == 'POST':
       selected_team = request.form.get('team_choice')
        #Redirects the user to the draft page.
       return redirect(url_for('draft'))

 #Render thje index.html template and gives the list of teams to the draft page.
   return render_template('index.html', teams=[team.team_name for team in NFL_teams])

#Route for the draft page where the draft simulation happens.
@app.route('/draft', methods=['GET', 'POST'])
def draft():
    #Accesses the prospect list and draft log.
    global prospect_list, draft_summary
    
    #Creates copy of draft log.
    filtered_prospects = prospect_list[:]  
    
    if selected_team:
        
        if not draft_summary:
            #Goes through the draft simulation process for each non-user team.
            for pick, team_name in draft_order.items():
                
                team = teams_draft_order[team_name]
                if team_name != selected_team:
                    # Goes through all of the prospects to increase team rating based on the need of each team.
                    for prospect in filtered_prospects:
                        prospect.team_rating = prospect.rating
                        if team.first_need == prospect.position:
                            prospect.team_rating += 3
                        elif team.second_need == prospect.position:
                            prospect.team_rating += 1
                    #Finds the best draft prospect for each team based on team need and overall rating of the prospect.
                    draft_pick = max(filtered_prospects, key=lambda p: p.team_rating)
                    #Removes the prospect fdrom both the list of availible player and removes the player from the global list aswell.
                    filtered_prospects.remove(draft_pick)
                    prospect_list.remove(draft_pick)
                    draft_summary.append(f"With the #{pick} pick, the {team_name} select {draft_pick.name}.")
                else:
                    #stops when it is the user's turn to pick.
                    break  

        # Handle user choices for sorting/filtering,
        if request.method == 'POST':
            choice = request.form.get('draft_choice')
            position_sort = request.form.get('position_sort')

            if choice == "1" and position_sort:
                # Sort by position.
                filtered_prospects = [p for p in filtered_prospects if p.position == position_sort]
            elif choice == "2":
                # Sort by overall prospect rating.
                bubble_sort(filtered_prospects, 'rating')
            elif choice == "3":
                # Sort by team rating.
                bubble_sort(filtered_prospects, 'team_rating')
            elif choice == "4":
                # Provide advice on best player based on team rating.
                best_draft_pick = max(filtered_prospects, key=lambda p: p.team_rating)
                draft_summary.append(f"The best draft pick for your team is {best_draft_pick.name} with a team rating of {best_draft_pick.team_rating}.")
            # If the user selects a player.
            if request.form.get('select_player'):
                selected_player = request.form.get('select_player')
                player = next((p for p in filtered_prospects if p.name == selected_player), None)

                if player:
                    try:
                        # Remove the user selected prospect from filter prospects and global list.
                        filtered_prospects.remove(player)
                        prospect_list.remove(player)  
                        draft_summary.append(f"With the #{len(draft_summary) + 1} pick, you selected {player.name}.")
                        
                        # Simulate the rest of team's draft picks after the user selects.
                        pick_number = len(draft_summary)  
                        for next_pick_number in list(draft_order.keys())[pick_number:]:
                            next_team = draft_order[next_pick_number]
                            next_team_obj = teams_draft_order[next_team]

                            for prospect in filtered_prospects:
                                prospect.team_rating = prospect.rating
                                if next_team_obj.first_need == prospect.position:
                                    prospect.team_rating += 3
                                elif next_team_obj.second_need == prospect.position:
                                    prospect.team_rating += 1

                            next_draft_pick = max(filtered_prospects, key=lambda p: p.team_rating)
                            #Removes selected prospect from both the list of firsted prospects and global list.
                            filtered_prospects.remove(next_draft_pick)
                            prospect_list.remove(next_draft_pick)  
                            draft_summary.append(f"With the #{next_pick_number} pick, the {next_team} select {next_draft_pick.name}.")

                    except Exception as e:
                        # Debugging log to catch any error with player removal.
                        print(f"Error removing player: {e}") 
        # Render the draft.html, passing the current list of prospects and draft log.
        return render_template('draft.html', prospects=filtered_prospects, draft_pick_info=draft_summary, user_team=selected_team, positions=positions)
    # Render the draft.html template before the user picks, showing available prospects and draft log.
    return render_template('draft.html', prospects=filtered_prospects, draft_pick_info=draft_summary, user_team=selected_team)


# Run the application in debug mode.
if __name__ == '__main__':
   app.run(debug=True)