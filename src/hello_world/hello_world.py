from inspirational_quotes import quote
from pyfiglet import Figlet
from wonderwords import RandomSentence


def hello_world():
    # var string ASCII art style Hello World
    f = Figlet(font='slant')
    styled_hw = f.renderText('Hello World')

    # var string Hello World
    plain_hw = "Here is the plain:\nHello World\n"

    # var string random quote
    q = quote()
    random_quote = f"Here's a random quote:\n{dict(q)['quote']}\n- {dict(q)['author']}\n"

    # var string random sentence
    s = RandomSentence()
    random_sentence = f"Here's a random sentence:\n{s.sentence()}"

    return styled_hw, plain_hw, random_quote, random_sentence
