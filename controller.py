import viginere
import input_handling

class controller():

    def secretWord(self):
        secret_word_list = []
        print('Enter secret word:')
        secret = input().lower()
        secret_word = secret.replace(" ", "")
        for letter in secret_word:
            secret_word_list.append(letter)
        return secret_word_list
    
    def search(self, list, letter):
        for i in range(len(list)-1):
            if list[i] == letter:
                return i 
            


    def encryption(self, plaintext, secret_word, table, keyed_list):
        cyphertext = ""
        for i in range(len(plaintext)-1):
            secret_word_index = self.search(keyed_list, secret_word[i%7])
            print(secret_word_index)
            plaintext_index = self.search(keyed_list, plaintext[i])
            cyphertext = cyphertext + table[secret_word_index][plaintext_index] + " "
        return cyphertext




    def main(self):
        secret_word = []
        PT = input_handling.plaintext()
        VT = viginere.viginere_table()
        plaintext = PT.get_plaintext()
        print(plaintext)
        secret_word = self.secretWord()
        print(secret_word)
        keyed_list = VT.keyed_list()
        print(keyed_list)
        table = VT.matrix(keyed_list)
        print(table)
        print (self.encryption(plaintext, secret_word, table, keyed_list))
        return 0
    
run = controller()
run.main()