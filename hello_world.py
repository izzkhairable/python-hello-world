from inspirational_quotes import quote
from pyfiglet import Figlet
from wonderwords import RandomSentence


def hello_world():
    f = Figlet(font='slant')
    print(f.renderText('Hello World'))
    q = quote()
    print(f"Here's a random quote:\n{dict(q)['quote']}\n- {dict(q)['author']}\n")
    s = RandomSentence()
    print(f"Here's a random sentence:\n{s.sentence()}")