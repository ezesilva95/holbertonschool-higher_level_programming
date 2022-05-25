#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation

text_indentation("What's my name you ask? Listen kid, my name is: The Great Ezequiel. And as you may have guessed, I am great.")

try:
    text_indentation(1)
except Exception as e:
            print(e)

try:
        text_indentation(None)
except Exception as e:
                print(e)

try:
        text_indentation([1])
except Exception as e:
                print(e)
