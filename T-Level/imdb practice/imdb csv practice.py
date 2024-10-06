import pandas as pd
import matplotlib.pyplot as plt

imdb = pd.read_csv("imdb_movie_list.csv")
space = "########################################"

"""
 1) filter some data
 2) get a list of movies for a specific year
 3) do some sort calculation with the data
 4) one should produce a graph
"""

# main menu for the program
def main_menu():
    # listing the available options
    print(f"{space}\n-----MAIN MENU-----\n\
1. Filter data\n\
2. List of movies from a specific year\n\
3. How much profit a movie made\n\
4. Graph of scores for a genre\n\
5. Quit\n{space}")

    # asking the user to input a number from the menu
    ask = input("Please enter a number: ").strip()
    ask = int(ask)

    if ask == 1:
        filter_data()
    elif ask == 2:
        movie_list()
    elif ask == 3:
        movie_profit()
    elif ask == 4:
        graph()
    elif ask == 5:
        print("Goodbye!")
        exit()
    else:
        print(f"{space}Please enter a valid number{space}")
        main_menu()

   


def filter_data():
    print(f"{space}\nThese are the top 10 horror movies")
    # first we are getting all the horror movies from the genre column. after that we are now getting the names, genre, date and score columns --
    # -- to print out so it looks neater to the user
    filtered_data = imdb.loc[imdb["genre"] == "Horror", ["names", "genre", "date_x", "score"]].head(10)
    # the code below is just getting rid of the index number that appear on the left side --
    # -- when printing a csv file
    print(filtered_data.to_string(index=False))
    # printing space to show its a new output
    print(space)
    # return to menu option

def movie_list():
    import datetime

    imdb["date_x"] = pd.to_datetime(imdb["date_x"])

    min = imdb["date_x"].min()
    max = imdb["date_x"].max()

    asking_year = input(f"\n{space}\nPlease enter a year ({str(min.year)} - {str(max.year)}): ")

    if asking_year.isdigit() == True:
        int_year = int(asking_year)
    else: 
        movie_list()

    try:
        year_start = datetime.datetime(int_year, 1, 1)
        year_end = datetime.datetime(int_year, 12, 31)
    except:
        print("test")
        # movie_list()

    if int_year < min.year or int_year > max.year:
        print(f"\n{space}Please enter a valid year\n{space}")
        movie_list()
    else:
        movie_by_year = imdb.loc[(imdb["date_x"] > year_start) & (imdb["date_x"] < year_end)]
        return movie_by_year

    

def movie_profit():
    #print("sdfssg")

def graph():
    #print("SDGSsg")


main_menu()