import viginere
import input_handling

class controller():
    def secretWord(self):
        secret_word_list = []
        print('Enter secret word:')
        secret = input()
        secret_word = secret.replace(" ", "")
        for letter in secret_word:
            secret_word_list.append(letter)
    
    def search(self, list, letter):
        for i in range(len(list)-1):
            if list[i] == letter:
                return[i]
            


    def encryption(self, plaintext, secret_word, table):
        cyphertext = ""
        for i in range(len(plaintext)-1):
            secret_word_index = self.search(secret_word, secret_word[i%7])
            plaintext_index = self.search(plaintext, plaintext[i])
            cyphertext = cyphertext + table[secret_word_index][plaintext_index] + " "
        return cyphertext




    def main(self):
        plaintext = input_handling.plaintext.get_plaintext()
        secret_word = self.secretWord()
        keyed_list = viginere.keyed_list()
        table = viginere.viginere_table.matrix(keyed_list)
        print (self.encryption(plaintext, secret_word, table))
        return 0
    

controller.main()