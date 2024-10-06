# NFL Draft Web Application

The NFL Draft Web Application is a web-based tool designed to simulate the experience of an NFL draft. Users can select an NFL team to control and participate in drafting players based on their team's needs. The application utilizes Python and Flask to provide a dynamic and interactive interface for managing the draft.
# Project Overview
This project allows users to control a NFL team during a draft while the remaining teams are simulated by the application. Users can sort and filter available players based on different attributes, such as position or rating, and draft the best available player for their team. The draft proceeds automatically for other teams, and their selections are logged and displayed for the user.
# Features
The NFL Draft Web Application offers several key features. Users can begin by selecting their favorite NFL team to control during the draft. Once the draft begins, the application automatically handles picks for the other teams based on their specific needs, with the user stepping in to make decisions for their chosen team.

During the draft, users have the option to sort and filter the list of available players by position, rating, or by how well they fit the team’s needs. If a user is unsure about which player to draft, the application provides advice on the best available player based on team requirements. Each pick is logged and displayed in real-time, offering a full draft experience.

# Getting Started
Before running the NFL Draft Web Application, you need to ensure that certain dependencies are installed. Specifically, you need to have Python 3.x and Flask installed on your system. To install Flask, simply run the command pip install flask in your terminal.
Once you have Flask installed, you can set up the application by cloning the repository. Navigate to the project directory and, if necessary, install any dependencies listed in the requirements.txt file using the command pip install -r requirements.txt. After that, run the command python app.py to start the Flask development server. The application should now be accessible at http://127.0.0.1:5000/ in your browser.

# File Structure
## app.py
This is the main Python script that runs the application. It handles all the core logic of the NFL Draft Simulator. Inside app.py, you will find:

- Flask Routing: Manages user requests and directs them to appropriate routes, such as the team selection page and the draft page.
- Classes: The Prospect and Team classes manage the data structure of individual players and teams. These classes define the attributes of each player, like position, rating, and height, as well as team needs, like first and second draft priorities.
- Draft Logic: The draft logic includes selecting players for AI-controlled teams, filtering and sorting prospects, and managing user picks. The draft progress is stored and updated throughout the user’s session.
- Form Handling: The application processes user selections through HTML forms submitted via POST requests, which Flask handles on the server side. This includes selecting a team, filtering prospects, and choosing a player during the draft.
templates/
This directory contains the HTML templates that are rendered by Flask and displayed to the user. The Flask framework uses Jinja2 templating, allowing you to dynamically inject content from the Python backend into the HTML pages.

## index.html: This is the homepage, where users can select their team from a dropdown list. The list of teams is dynamically populated by Flask based on data passed from the app.py.
## draft.html: This is the draft interface where users participate in the draft. It displays the available prospects, the draft log (showing previous picks), and the form where users can sort, filter, and select players during the draft. It also allows for real-time updates based on the draft’s progression.
