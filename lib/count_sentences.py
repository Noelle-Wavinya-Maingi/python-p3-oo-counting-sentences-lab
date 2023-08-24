class MyString:
    def __init__(self, value=''):
        self._value = None
        self.set_value(value)

    def get_value(self):
        return self._value

    def set_value(self, new_value):
        if type(new_value) == str:
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        pattern_punctuation = ['.', '!', '?']
        sentences = self._value.split('\n')  
        sentence_count = 0

        for sentence in sentences:
            sentence = sentence.strip()  
            if any(sentence.endswith(punctuation) for punctuation in pattern_punctuation):
                sentence_count += 1

        return sentence_count

    value = property(get_value, set_value)
