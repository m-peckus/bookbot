
def main():
    print("---Print report of books/frankenstein.txt---")
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    print('\n')
   
    alphabet_string = alpha_string(text)
    dictionary = make_dictionary(alphabet_string)
    list_dict = convert(dictionary)
    
#use sort() method to sort over list of dictionaries
    list_dict.sort(reverse=True, key=sort_on) 

 #iterate over list of dictionaries & print final report
    iterate_list_dict(list_dict)

#sort list of dictionaries by value (key: value:)
def sort_on(dict):
    values = list(dict.values())
    return values

#iterate over list of dictionaries
#print final report
def iterate_list_dict(input_dictionary):
    for item in input_dictionary:
        for i in item:
            a = i
            b = item[i]
            print(f"The '{a}' character was found {b} times")
        
    print("---End Report---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read().lower()

def get_num_char(text):
    string = text.lower()
    myDict = {}
    for item in string:
        if item not in myDict:
            myDict[item] = 1
        else:
            myDict[item] += 1
    return myDict

#remove non alphabetic characters
def alpha_string(string):
        alphabetic_string= ""

        for a in string:
            if (a.isalpha()) == True:
                 alphabetic_string+=a    
    
        return alphabetic_string

#create dictionary
def make_dictionary(string):
        myDict = {}
          
        for item in string:
            if item not in myDict:
                myDict[item] = 1
            else:
                myDict[item] += 1

        return(myDict)   

#create list of dictionaries
def convert(dictionary):
  return [{key: value} for key, value in dictionary.items()]

main()




