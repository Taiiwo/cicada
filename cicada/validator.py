import os

class Validator:
    def __init__(self):
        self.alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + ' '
        with open(os.path.join(os.path.dirname(__file__), 'cicadict.txt')) as f:
            self.cicadian_words = f.read().split("\n")

    def get_english_count(self, message):
        message = message.upper()
        message = self.remove_non_letters(message)
        possible_words = message.split()

        if len(possible_words) == 0:
            return 0.0 # no words at all, so return 0.0

        matches = 0
        for word in possible_words:
            if word in self.cicadian_words:
                matches += 1
        return float(matches) / len(possible_words)


    def remove_non_letters(self, message):
        letters_only = []
        message = message.upper()
        for symbol in message:
            if symbol in self.alpha:
                letters_only.append(symbol)
        return ''.join(letters_only)


    def is_cicadian(self, message, word_percentage=20, letter_percentage=85):
        # By default, 20% of the words must exist in the dictionary file, and
        # 85% of all the characters in the message must be letters or spaces
        # (not punctuation or numbers).
        words_match = self.get_english_count(message) * 100 >= word_percentage
        num_letters = len(self.remove_non_letters(message))
        message_letters_percentage = float(num_letters) / len(message) * 100
        letters_match = message_letters_percentage >= letter_percentage
        return words_match and letters_match
