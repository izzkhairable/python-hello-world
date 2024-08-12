from inspirational_quotes import quote
from pyfiglet import Figlet
from wonderwords import RandomSentence


def hello_world():
    # Print out ASCII art style Hello World
    f = Figlet(font='slant')
    print(f.renderText('Hello World'))

    #  Print out a plain Hello World
    print(f"Here is the plain:\nHello World\n")

    # Print out a random quote
    q = quote()
    print(f"Here's a random quote:\n{dict(q)['quote']}\n- {dict(q)['author']}\n")

    # Print out a random sentence
    s = RandomSentence()
    print(f"Here's a random sentence:\n{s.sentence()}")