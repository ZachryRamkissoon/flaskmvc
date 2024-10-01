import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User, Competition, Result, Admin
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize, get_all_competitions, get_user_by_username, get_student_results, create_admin, create_competition, get_admin_by_username, get_competitions_by_admin, 
get_competition_results, import_results, get_all_competitions, get_all_admins_json)


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())


@user_cli.command("viewCompetitions", help="View Competitions")
def view_competitions():
    competitions = get_all_competitions()
    for competition in competitions:
        print(competition.get_json())

@user_cli.command("viewCompetitionResults", help="View competition results (flask student viewCompetitionResults <competition_id>)")
@click.argument("comp_id", default="1")
def view_competition_results(competition_id):
    results = get_competition_results(competition_id)
    for result in results:
        print(result.get_json())

app.cli.add_command(user_cli) 


admin_cli = AppGroup('admin', help='Admin object commands')

@admin_cli.command("create", help="Creates an admin")
@click.argument("username", default="admin")
@click.argument("password", default="adminpass")
def create_user_command(username, password):
    create_admin(username, password)
    print(f'{username} created!')

@admin_cli.command("list", help="Lists admins in the database")
@click.argument("format", default="string")
def list_user_command(format):
    print(get_all_admins_json())                                                              

@organizer_cli.command("createCompetition", help="Creates a competition (flask admin createCompetition <username> <CompetitionName> <description>)")
@click.argument("username", default="admin")
@click.argument("name", default="competition")
@click.argument("description", default="description")
def create_competition(username, name, description):
    admin = get_admin_by_username(username)
    create_competition(admin.admin_id, name, description)
    print("Created Successfully")

@admin_cli.command("viewCompetitions", help="View Admin's Competitions (flask admin viewCompetitions <username>)")
@click.argument("username", default="admin")
def view_competitions_admin(username):
    admin = get_admin_by_username(username)
    competitions = get_competitions_by_admin(admin.admin_id)
    for competition in competitions:
        print(competition.get_json())                                       

@admin_cli.command("viewCompetitionResults", help="View Admin's Competition Results (flask admin viewCompetitionResults <username>)")
@click.argument("username", default="admin")
def view_competition_results_admin(username):
    admin = get_admin_by_username(username)
    competitions = get_competitions_by_admin(admin.admin_id)
    for competition in competitions:
        results = get_competition_results(competition.competition_id)
        for result in results:
            print(result.get_json())                              

@admin_cli.command("importResults", help="Import Results from CSV (flask admin importResults <competition_id> <filePath>)")
@click.argument("competition_id", default="1")
@click.argument("file", default="./App/controllers/scores.csv")
def importResults(competition_id, file):
    import_results(competition_id, file)                                          //working

app.cli.add_command(organizer_cli)


'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)