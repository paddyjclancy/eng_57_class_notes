voting_age = 18
driving_age = 17
drinking_age = 16

# age = 19
# driver_licence = True


# - You can vote and drive
# - You can vote
# - You can drive
# - you can't legally drink but your mates/uncles might have your back (bigger than 16)
# - You're too young, go back to school!
# As a user I should be able to keep being prompted for input until I say 'exit'

age = int(input("What is your age?  "))

if age >= 18:
    print("You are old enough to vote in the UK... do!")

if age >= 17:
    print("You are old enough to get a UK driver's licence.")

if age >= 16:
    print("You are old enough to drink in the UK. If you are under 18 however this may only be done if specific conditions have been met.... we'll be watching you.")

else:
    print("You are not of legal age. \nContinue to enjoy childhood / adolescence while you can, and do not concern yourself with the toils of adulthood just yet!")



# if age >= 16:
#     drink = True
# elif age >= 17:
#     drive = True
# elif age >= 18:
#     vote = True
#
# if drink == True:
#     print("You are old enough to drink under the UK. If you are under 18 however this may only be done if specific conditions have been met.... we'll be watching you.")
#
# if drive == True:
#     print("You are old enough to get a UK driver's licence.")
#
# if vote == True:
#     print("You are old enough to vote in the UK... do!")