# Mad libs game again

#adjective = input("Enter adjective = \n")
#pokemon_type = input("Enter a Pokemon type = \n")
#fav_Pokemon = input("Enter your favourite Pokemon = \n")

#print("I think " + pokemon_type + " Pokemon are " + adjective + " but " + fav_Pokemon + " is my favourute!")

JoJo_dictionary = {
        "Phantom Blood" : "Jonathan Joestar, Dio Brando, Baron Zeppeli, Erina, Poco",
        "Battle Tendancy" : "Joseph Joestar, Ceaser, Strotenhiem, Suzie Q, Lisa Lisa",
        "Startdust Crusaders" : "Jotaro Kujo, Joseph Joestar, Muhammed Avdol, Jean-Pierre Polanareff, Kakyoin",
        "Diamond is Unbreakable" : "Josuke Higashkata, Jotaro Kujo, Okaysu, Koichi",
        "Golden Wind" : "Giorno Giovanna, Bruno Buccarati, Abachio, Narancia, Fugo, Mista",
}

print(JoJo_dictionary.get("Phantom Blood", "That is not a JoJo part my bro..."))