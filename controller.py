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
            
    def search_for_letter(self, list, letter, table):
        print(list)
        for i in range(len(list)-1):
            print("index: " + str(i) + " looking for: " + letter)
            if list[i] == letter:
                return table[i][0]

    def encryption(self, plaintext, secret_word, table, keyed_list):
        cyphertext = ""
        for i in range(len(plaintext)):
            secret_word_index = self.search(keyed_list, secret_word[i%(len(secret_word))])
            plaintext_index = self.search(keyed_list, plaintext[i])
            cyphertext = cyphertext + table[secret_word_index][plaintext_index] + " "
        return cyphertext
    
    def decryption(self, cyphertext, secret_word, table, keyed_list):
        plaintext = ""
        for i in range(len(cyphertext)):
            keyed_list_index = self.search(keyed_list, secret_word[i%(len(secret_word))])
            plaintext = plaintext + self.search_for_letter(table[keyed_list_index], cyphertext[i], table) + " "
        return plaintext

    def main(self):
        secret_word = []
        PT = input_handling.text()
        VT = viginere.viginere_table()
        CT = input_handling.text()
        secret_word = self.secretWord()
        keyed_list = VT.keyed_list()
        table = VT.matrix(keyed_list)
        i = 0
        while i < 1:
            print('Encryption or Decryption (e/d)? ')
            answer = input().lower()
            if answer == 'e':
                i = i+1
                plaintext = PT.get_plaintext()
                print (self.encryption(plaintext, secret_word, table, keyed_list))
            elif answer == 'd':
                i = i+1
                cyphertext = CT.get_cyphertext()
                print (self.decryption(cyphertext, secret_word, table, keyed_list))
        return 0
    
run = controller()
run.main()