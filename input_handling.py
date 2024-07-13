class plaintext():

    def remove_spaces(self, word):
        return word.replace(" ", "")
    
    def get_plaintext(self):
        plaintext = []
        print("Enter plaintext: ")
        plaintext_initial = input().lower()
        plaintext_smush = self.remove_spaces(plaintext_initial)
        for letter in plaintext_smush:
            plaintext.append(letter)
        return plaintext
    
    