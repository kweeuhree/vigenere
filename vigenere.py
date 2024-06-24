import time 

# valid yes answers
valid_yes_answers = ['yes', 'y']

# - encode logic -------------------------------------------------------------------------
def encode_message(message_to_encode, keyword):
    print('\nEncoding...')
    time.sleep(1)

    reference = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # create an encoding string using keyword

    keyword_string = ''
    keyword_index = 0
    for char in message_to_encode:
        if char.isalpha():
            keyword_string += keyword[keyword_index]
            keyword_index = (keyword_index + 1)%len(keyword)
        else:
            keyword_string += char
    
    # iterate through message // shift message letter by keyword letter
    encoded_message = ''
    for i, char in enumerate(message_to_encode):
        if char.isalpha():
            char_index = reference.index(char)
            keyword_string_index = reference.index(keyword_string[i])
            encoded_message_index = (char_index + keyword_string_index) % 26
            encoded_message += reference[encoded_message_index]
        else:
            encoded_message += char
    
    
    print('\n', encoded_message)
    continue_prompt()

def encoding():
    message_to_encode = get_message()
    keyword = get_keyword()
    encode_message(message_to_encode, keyword)

# -------------------------------------------------------------------- end encode logic -
# - decode logic -------------------------------------------------------------------------
def decode_message(message_to_decode, keyword):
   time.sleep(1)
   print("\nDecoding...")

   reference = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

   #create a string to decode the message
   def find_keyword_string(keyword):
         keyword_string = ''
         keyword_index = 0
         for char in message_to_decode:
            if char.isalpha():
               keyword_string += keyword[keyword_index]
               keyword_index = (keyword_index + 1) % len(keyword)   
            else:
               keyword_string += char
         return keyword_string
   
   #find a new index to decode the message
   keyword_message = find_keyword_string(keyword)  
   decoded_message = ''
   for i, char in enumerate(message_to_decode):
      if char.isalpha():
         message_index = reference.index(char)
         keyword_message_index = reference.index(keyword_message[i]) 
         result_index = (message_index - keyword_message_index) % 26
         decoded_message += reference[result_index]
      else:
         decoded_message += char

   print('\n', decoded_message)
   continue_prompt()

def decoding():
    message_to_decode = get_message()
    keyword = get_keyword()
    decode_message(message_to_decode, keyword)

# -------------------------------------------------------------------- end decode logic -

# def repeat():
#     time.sleep(1)
#     print('\nWould you like to exit?\nEnter yes or no: ', end="")
#     answer = input().lower()
#     if answer in valid_yes_answers:
#         print('\nEnd of session.')
#     else:
#         main()


def get_message():
    print('\nPlease enter message to encode: ', end='')
    message_to_encode = input().lower()

    return message_to_encode


def get_keyword():
    print('\nPlease enter keyword for encoding: ', end='')
    keyword = input().lower()

    return keyword


def continue_prompt(): 
    time.sleep(1)
    print("\nWould you like to try again?\nEnter Y to continue or X to exit:\n", end='')
    answer = input().lower()
    if answer in valid_yes_answers:
        main()
    else:
        print('\nEnd of session.')

def main():
    print("\nWould you like to encode or decode a message?\nEnter E to encode or D to decode:\n", end='')
    type = input().lower()
    if type == 'e':
        encoding()
    elif type == 'd':
        decoding()
    else:
        continue_prompt()

if __name__ == "__main__":
  while True:
    print('\nHello!')
    main()

    break