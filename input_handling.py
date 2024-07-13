class text():

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
    
    def get_cyphertext(self):
        cyphertext = []
        print("Enter cyphertext")
        cyphertext_initial = input().lower()
        cyphertext_smush = self.remove_spaces(cyphertext_initial)
        for letter in cyphertext_smush:
            cyphertext.append(letter)
        return cyphertext
    
    