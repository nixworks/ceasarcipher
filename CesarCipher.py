# coding=utf-8


class CesarCipher(object):
    _alphabet = None
    _shift = None

    def set_alphabet(self, value):
        self._alphabet = value

    def set_shift(self, value):
        self._shift = value

    def move_right_or_go_to_start(self, value):
        """
        Function that will allow us to turn to the start of alphabet,
        if shifted index is out of range

        Это функция, которая позволить возвращатся в начало алфавита,
        если сдвиг вправо невозможен из-за отсутствия следующих букв

        """
        index_in_alphabet = self._alphabet.index(value)
        last_index_of_alphabet = len(self._alphabet) -1
        shifted_index = index_in_alphabet + self._shift
        if not shifted_index > last_index_of_alphabet:
            shifted_letter = self._alphabet[index_in_alphabet + self._shift]
        else:
            delta = shifted_index - last_index_of_alphabet
            shifted_letter = self._alphabet[delta - 1]
        return shifted_letter

    def encode(self, plain_text):
        result_text = ''
        for letter in plain_text:
            if letter == ' ':
                result_text += letter # Пробел оставляем пробелом
            elif letter in self._alphabet:
                shifted_letter = self.move_right_or_go_to_start(letter) # Призываем функцию выше
                result_text += shifted_letter
            else:
                result_text += letter
        return result_text


alphabet = []

for i in range(ord('a'),ord('z')+1):
    alphabet.append(chr(i))

text = raw_input('Please enter your string: ')
shift = int(raw_input('Please enter a shift value(must be an integer): '))

instance = CesarCipher()
instance.set_alphabet(alphabet)
instance.set_shift(shift)
print instance.encode(text)
