<h1>Message Encoder/Decoder</h1>
<hr>
<p>This Python script allows to encode or decode messages using a keyword-based cipher. It provides a command-line interface for user interaction.</p>
<ul>Features:</ul>
<li>Encoding and Decoding: Choose between encoding and decoding a message.</li>
<li>Keyword Input: Enter a keyword to modify the encoding pattern.</li>
<li>Interactive Interface: Continuously prompts the user for new messages until they choose to exit.</li>
<li>Human-like Interaction: Uses time delays to simulate a more natural interaction flow.</li>
<br>
<p>To run this program, users will need a Python-friendly environment.</p>

<hr>
<p>This script has gone through several development stages and has been continuously modified throughout my programming journey. The latest version is optimized with best practices including maintainability, reusability, and DRY (Don't Repeat Yourself).</p>
<p>What used to be multiple repeating funtions is now two organized <code>process_message</code> and <code>get_keyword_string</code> functions:</p>
<code>process_message:

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

</code>
<br>
<code>get_keyword_string:

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

</code>