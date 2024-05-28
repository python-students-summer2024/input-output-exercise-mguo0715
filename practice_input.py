"""
A little assignment to practice receiving text input from the user in Python programming.
Do not run this file... run main.py instead.
"""


def get_favorite_vegetable():
    """
    Asks the user to enter their favorite vegetable
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite vegetable.
    """
    # Adding variable 'vegetable' encoding favorite veggie and returning with statement 

    vegetable = input("Input your favorite vegetable")
    print("Interesting! I also love " + vegetable + "!")


def get_favorite_number():
    """
    Asks the user to enter their favorite number
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite number.
    """
    # Requesting favorite number and outputting in statement

    fav_number = input("What's your favorite number?")
    print("Interesting! I also love " + fav_number + "!")


def get_name_and_zodiac_sign():
    """
    Asks the user to enter their name.
    Then ask them to enter their zodiac sign.
    Then print out, "Interesting! My name is also X, and I'm also a Y!",
    where X and Y are replaced by the user's name and zodiac sign, respectively.
    """
    # Requesting name + zodiac, and outputting in statement
    name = input("What's your name?")
    zodiac = input("What's your Zodiac Sign?")
    print("Interesting! My name is also " +
          name + 
          ", and I'm also a " + 
          zodiac + "!")


def get_name_and_age():
    """
    Asks the user to enter their name.
    Then ask them to enter their age.
    Then print out, "Interesting! My name is also X, and I'm also Y years old!",
    where X and Y are replaced by the user's name and age, respectively.
    """
    # Requesting name + age, and outputting in statement

    name = input("what's your name")
    age = input("what's your age")
    print("Interesting! My name is also " + 
          name + 
          ", and I'm also " +
          age + 
          " years old!")
