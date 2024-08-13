from hello_world.hello_world import hello_world


def main():
    styled_hw, plain_hw, random_quote, random_sentence = hello_world()
    print(styled_hw)
    print(plain_hw)
    print(random_quote)
    print(random_sentence)


if __name__ == "__main__":
    main()
