class paintext():

    def remove_spaces(self, string):
        return string.replace(" ", "")
    
    def get_plaintext(self):
        plaintext = []
        print("Enter plaintext: ")
        plaintext_initial = input().lower()
        plaintext_smush = self.remove_spaces(plaintext_initial)
        for letter in plaintext_smush:
            plaintext.append(letter)
        return plaintext
    
    