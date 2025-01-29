# Define the function to create a congratulations message
def create_congratulations_message(name, achievement):
    return f"Congratulations {name.capitalize()} on your {achievement.capitalize()}! We are proud of you!"

# Get user input
name = input("Please enter your name: ")
achievement = input("Please enter your achievement: ")

# Generate and display the message
message = create_congratulations_message(name, achievement)
print(message)
