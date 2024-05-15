#!/usr/bin/env python3

class MyString():

    def __init__(self, value=""):
        # value is a property, check if value is a string
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        # returns True if value ends in a period, else False
        # endswith() does not return True if there is spaces after dot.Use strip() before checking for dot.
        stripped_value = self._value.strip()
        if stripped_value.endswith("."):
            return True
        else:
            return False

    def is_question(self):
        # returns True if value ends in a question mark, else False
        stripped = self._value.strip()
        if stripped.endswith("?"):
            return True
        else:
            return False

    def is_exclamation(self):
        stripped_one = self._value.strip()
        if stripped_one.endswith("!"):
            return True
        else:
            return False

    def count_sentences(self):
        # Replace multiple dots or exclamation marks with a single dot
        value = self._value.replace("...", ".")
        # breakpoint()
        value2 = value.replace("!!", ".")
        value3 = value2.replace("?", ".")
        # breakpoint()
    # Split the text into sentences
        sentences = [sentence.strip()
                     for sentence in value3.split(".") if sentence.strip()]
    # Count the number of sentences
        # breakpoint()
        return len(sentences)


# edge case as below:
text = "This, well, is a sentence. This is too!! And so is this, I think? Woo..."
v = MyString(text)
print(v.count_sentences())
