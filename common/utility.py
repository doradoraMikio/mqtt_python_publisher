from datetime import datetime
import random
import string

BLANK = ""
SPACE = " "


class Common:

    @staticmethod
    def get_time_stamp():
        return datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    @staticmethod
    def get_random_words(word_length : int, word_number : int):
        words = ""

        for index in range(word_number):
            word = BLANK.join(random.sample(string.ascii_letters, k=word_length))
            words += word + SPACE
        return words


