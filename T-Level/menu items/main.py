try:
    import pandas as pd
    import datetime
    import matplotlib.pyplot as plt
except Exception:
    print("Library not working.")
    exit()

space = "########################"

'''
Display the latest sales for the a specific product (based on the user's input)
Create a list of the top 10 products
Create a graph to display the products sales (user input) over time sort from earliest to latest
Create a graph that will show the sales for all products between two specified dates
'''
def main_menu():
    while True:
        print(f"{space}\n1. Display latest sales\n2. list of top 10 products\n3. Graph of selected item\n4. Graph for all products between dates\n5. Quit\n{space}")
        ask = input("Please enter a choice (1 - 5): ")

        try:
            int(ask)
            
        except:
            print(f"\n{space}\nPlease enter a valid number\n")
            continue
        else:
            ask = int(ask)
            if ask == 1:
                latest_sales()
            elif ask == 2:
                top_ten()
            elif ask == 3:
                graph_selected_item()
            elif ask == 4:
                graph_all_between_dates()
            elif ask == 5:
                print(f"\n{space}\nExiting...\n{space}")
                exit()
            else:
                print(f"\n{space}\nPlease enter a number from 1 - 5\n")

def latest_sales():
    data = pd.read_csv("menu_itemsss.csv")
    index = 1
   
    print(space)

    for item in data["Menu Items"]:
        print(f"• {index}) {item}")
        index += 1
    
    while True:
        get_menu_item = input("Please pick a number (1 - 17): ")

        try:
            int(get_menu_item)
            
        except ValueError:
            print(f"\n{space}\nPlease enter a valid number\n{space}\n")
        else:
            get_menu_item = int(get_menu_item)
            if (get_menu_item < 1 or get_menu_item > 17):
                print ("Please enter a number between (1 - 17)")
                continue
            else:
                latest_sales = data.iloc[get_menu_item - 1, :-6:-1]
                print (latest_sales)
               
                xaxis = latest_sales.index
                yaxis = latest_sales.values

                plt.plot(xaxis, yaxis)
                plt.xlabel("dates")
                plt.ylabel("sales")
                plt.show()

                return_main_menu()


def top_ten():
    data = pd.read_csv("menu_itemsss.csv")
    data["Total"] = data.iloc[:, 1:].sum(axis=1)

    sorted_data = data.sort_values(["Total"], ascending=False)

    print(sorted_data[["Menu Items", "Total"]].head(10))




def return_main_menu():
    while  True:
        return_menu = input(f"{space}\nWould you like to return to the main menu? (yes/no): ")

        return_menu = return_menu.lower()
        if return_menu == "yes":
            main_menu()
        elif return_menu == "no":
            print(f"{space}\nExiting...\n{space}")
            exit()
        else:
            print("Please enter a 'yes' or 'no': ")

            


main_menu()

