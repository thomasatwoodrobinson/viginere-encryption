class viginere_table():
        
    global abc
    abc = ['a','b','c','d','e','f','g','h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    def keyed_list(keyword):
        keyed_list = list()
        for letter in keyword:
            keyed_list.append(letter)
        

        for i in range(26):
            for existing_letter in keyed_list:
                if existing_letter == abc[i]:
                    i = i+1
                    break
                elif existing_letter == keyed_list[-1]:
                    keyed_list.append(abc[i])
        return keyed_list
    
    def matrix(keyed_list):
        matrix = []

        for i in range(26):
            new_row = []
            j = i
            while j < 26:
                new_row.append(keyed_list[j])
                j = j+1
            start = 0
            while len(new_row) < 26:
                new_row.append(keyed_list[start])
                start = start + 1
            matrix.append(new_row)
            print(new_row)
        
        return matrix
    

class main():
    
    keyed_list = viginere_table.keyed_list('love')
    matrix = viginere_table.matrix(keyed_list)
    #print(matrix)

main()