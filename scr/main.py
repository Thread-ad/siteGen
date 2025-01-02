from textnode import TextType, TextNode


def main():

    test_book = TextNode("The Wizard's Guide", TextType.NORMAL_TEXT, "https://bootdev.com")

    print(test_book)

if __name__ == "__main__":
    main()
