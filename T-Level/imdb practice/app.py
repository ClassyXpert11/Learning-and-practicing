import pandas as pd

def get_choice():
    '''
    A function that checks the choice from the menu    
    '''
    while True:
        
        choice = input("Please select from the options above (1-4): ")

        # Validate user choice

        try: 
            int(choice)
        except: 
            print ("Please input a number")
        finally:
            choice = int(choice)
            if (choice < 1) or (choice > 4):
                print ("Please enter a number from the options")
            else:
                return choice

def filter_by_rating():

    movies = pd.read_csv("data.csv")

    while True:
        user_input = input("Please enter a number between 0 - 100: ")

        try: 
            int(user_input)
        except: 
            print ("Please input a number")
        finally:
            user_input = int(user_input)
            if (user_input < 0) or (user_input > 100):
                print ("Please enter a number between 0 - 100")
            else:
                movies_above_rating = movies.loc[movies['score'] > user_input]
                return movies_above_rating

def filter_by_year():
    
    import datetime

    movies = pd.read_csv("imdb_movie_list.csv")

    movies["date_x"] = pd.to_datetime(movies['date_x'])

    min = movies["date_x"].min()
    max = movies["date_x"].max()
    
    while True:
        year = input ("Please select a year ("+ str(min.year) +" - "+ str(max.year) +"): ")
        #year = input (f"Please select a year ({str(min.year)} - {str(max.year)}): ")

        try: 
            int(year)
        except:
            print ("The input year must be a number")
            continue
        finally:
            year = int(year)

            if (year < min.year or year > max.year):
                print ("The input year must be between " + min.year + " and " + max.year)
                continue
            else:
                
                start_date = datetime.datetime(year, 1, 1)
                end_date = datetime.datetime(year, 12, 31)

                movies_by_year = movies.loc[(movies["date_x"] > start_date) & (movies["date_x"] < end_date)]

                return movies_by_year
            


def calculate_profit(movies):
    
    import matplotlib.pyplot as plt
    import numpy as np
    movies["profit"] = movies["revenue"] - movies["budget_x"]

    profits = movies["profit"].head()
    names = movies["names"].head()

    plt.xlabel("Movie Names")
    plt.ylabel("Profits (in millions)")
    plt.title("Total Profit for Movies in " + str(movies["date_x"].min().year))

    plt.bar(names, profits)
    plt.show()


def main_menu():
    while True:
        print ("Welcom to IMDB")

        print ("Main Menu")

        print ("1) Filter by Rating \n" +
            "2) Filter by Year \n" + 
            "3) Profit / Loss for a specific movie \n" + 
            "4) Exit")
        
        choice = get_choice()

        if (choice == 1):
            # run filter_by_rating function
            print (filter_by_rating())
        elif (choice == 2):
            # run filter_by_year function
            print(filter_by_year())
        elif (choice == 3):
            # run calculate_profit function

            movies_for_year = filter_by_year()

            calculate_profit(movies_for_year)
        else:
            exit()

main_menu()


