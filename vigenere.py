#add time to make the program look more human
import time 

# alphabet reference
reference = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# valid yes answers
valid_yes_answers = ['yes', 'y']

# - process logic -------------------------------------------------------------------------
def process_message(type, process):
    message_to_process = get_message()
    keyword = get_keyword()

    print("\n", process)
    time.sleep(1)

    # get keyword string
    keyword_string = get_keyword_string(message_to_process, keyword)  

    # initialize resultant message string
    resultant_message = ''
    # loop through message to process
    for i, char in enumerate(message_to_process):
        # if current character is alphabetic
        if char.isalpha():
            # get corresponding alphabetic reference index
            message_index = reference.index(char)
            # get corresponding alphabetic reference keyword index
            keyword_string_index = reference.index(keyword_string[i]) 
            # shift message letter by keyword letter, wrap around the alphabet
            if type == '+':
                result_index = (message_index + keyword_string_index) % 26
            elif type == '-':
                result_index = (message_index - keyword_string_index) % 26
            # add character to encoded message string
            resultant_message += reference[result_index]
        # else add current character to decoded message
        else:
            resultant_message += char

    print('\n', resultant_message)
    continue_prompt()
# -------------------------------------------------------------------- end process logic -
# - keyword logic -------------------------------------------------------------------------
# Function to create a string to decode the message
def get_keyword_string(message, keyword):
    #initialize keyword string and index
    keyword_string = ''
    keyword_index = 0
    # loop through message to decode
    for char in message:
        # if current character is alphabetic
        if char.isalpha():
            # add to keyword string
            keyword_string += keyword[keyword_index]
            # increment keyword index
            keyword_index = (keyword_index + 1) % len(keyword)  
         # else add curent character to keyword string 
        else:
            keyword_string += char
    
    return keyword_string
# -------------------------------------------------------------------- end keyword logic -

# Function to get the message from the user
def get_message():
    print('\nPlease enter message to encode: ', end='')
    message_to_encode = input().lower()

    return message_to_encode

# Function to get the keyword from the user
def get_keyword():
    print('\nPlease enter keyword for encoding: ', end='')
    keyword = input().lower()

    return keyword

# Function to prompt the user to continue or exit
def continue_prompt(): 
    time.sleep(1)
    print("\nWould you like to try again?\nEnter Y to continue or X to exit:\n", end='')
    answer = input().lower()
    if answer in valid_yes_answers:
        main()
    else:
        print('\nEnd of session.')

# Main function to start the program
def main():
    print("\nWould you like to encode or decode a message?\nEnter E to encode or D to decode:\n", end='')
    type = input().lower()
    if type == 'e':
        process_message('+', 'Encoding...')
    elif type == 'd':
        process_message('-', 'Decoding...')
    else:
        continue_prompt()

if __name__ == "__main__":
  while True:
    print('\nHello!')
    main()

    break