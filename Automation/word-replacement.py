def replace_word():
    str = "Hi guys, i am randall, and hi hi hi hi"
    print(str)
    word_to_replace = input("Enter the word to replace > ")
    word_replacement = input("Enter the word replacement > ")
    print(str.replace(word_to_replace, word_replacement))

replace_word()