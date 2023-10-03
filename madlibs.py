# TODO: Make a window to display and play other simple Python games
# TODO: Search for a database of MadLibs Prompts to randomly choose from -
# TODO: Auto-Generate MadLibs


loop = 0
while (loop < 9):
# Questions that will be asked of the user
    noun      = input("Choose a noun: ")
    p_noun    = input("Choose a pronoun: ")
    noun2     = input("Choose another noun: ")
    place     = input("Choose a place: ")
    adjective = input("Choose an adjective: ")
    noun3     = input("Choose yet another noun: ")

# Displays the story based on the user's input
    print("-------------------------------------------")
    print("Be kind to your",noun,"-footed",p_noun)
    print("For a duck may be somebody's",noun2,",")
    print("Be kind to your",p_noun,"in",place)
    print("Where the weather is always",adjective,".")
    print()
    print("You may think that is the the",noun3,",")
    print("well it is.")
    print("-------------------------------------------")
    loop += 1