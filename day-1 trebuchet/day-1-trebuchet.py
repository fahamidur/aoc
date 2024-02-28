def replace_with_number(string):
    string = str(string)
    string = string.lower()
    dict = {'one':'1','two':'2','three':'3','four':'4', 
            'five': '5', 'six': '6', 'seven': '7',
            'eight': '8','nine': '9'}
    for key in dict:
        value = dict[key]
        middle_index = len(key) // 2
        replacement = key[:middle_index] + value + key[middle_index + 1:]
        string = string.replace(key, replacement)
    return string

def return_number(string):
    number = ''
   
    string = replace_with_number(string)
    for i in string:
        if i.isdigit():
            number += i
    
    if len(number) > 1:
        return number[0]+number[-1]
    if len(number) == 1:
        return number + number 
    else:
        return 0
    
if __name__ == "__main__":

    f = open('input.txt','r')

    lines = f.readlines()

    result = 0
    for i in lines:
        result += int(return_number(replace_with_number(i)))
    print (result)



