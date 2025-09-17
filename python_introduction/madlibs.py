adj1 = input("Enter an adjective:  ")
adj2 = input("Enter another adjective:  ")
adj3 = input("Enter a third adjective:  ")
adj4 = input("Enter a fourth adjective:  ")


#Build the story template

story = (
        f"On a beatiful {adj1} day, I went to the zoo. "
        f"I saw a funny {adj2} monkey swinging from the trees. "
        f"Then, I spotted a majestic {adj3} lion lounging in the sun. "
        f"What a wild and {adj4} experiece!"
)


# Display the  final story
print("\nHere's your Mad Libs story: ")
print(story)
