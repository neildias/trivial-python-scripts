import string, random

builtin_key = {
    0: '`', 1: 'X', 2: 'G', 3: ':', 4: 'P', 5: 'e', 6: 'i', 
    7: 'a', 8: 'U', 9: '@', 10: 'm', 11: ']', 12: '%', 13: 'Y', 14: '/', 
    15: 't', 16: ')', 17: 'y', 18: 'M', 19: '{', 20: '#', 21: '*', 22: 'k', 
    23: 'E', 24: 'b', 25: 'L', 26: '^', 27: 'x', 28: '=', 29: '+', 30: 'Z', 
    31: 'c', 32: 'F', 33: '(', 34: 'u', 35: 's', 36: '[', 37: '_', 38: '\\', 
    39: 'V', 40: '}', 41: ',', 42: 'R', 43: '>', 44: 'Q', 45: '.', 46: 'I', 
    47: 'C', 48: 'J', 49: 'O', 50: ';', 51: '?', 52: '$', 53: 'w', 54: 'l', 
    55: 'g', 56: 'S', 57: 'D', 58: '<', 59: 'N', 60: '&', 61: 'B', 62: '!', 
    63: 'K', 64: 'q', 65: 'd', 66: 'T', 67: ' ', 68: 'o', 69: '-', 70: 'h', 
    71: '|', 72: 'W', 73: 'A', 74: 'f', 75: 'n', 76: 'r', 77: "'", 78: 'j', 
    79: 'H', 80: 'z', 81: '~', 82: '"', 83: 'v', 84: 'p'
}


key_list = [i for i in (string.ascii_letters + string.punctuation + " ")]
random.shuffle(key_list)



# index of alphabets dict
index_alphabet = dict(
    enumerate(
        # capture lower+upper alpha, punc and space
        string.ascii_letters + string.punctuation + " "
        # key_list    #instead of the above - may need to keep the index at +/-84
    )
)

# reverse dict of above
alphabet_index = {v:k for k, v in index_alphabet.items()}


def validate(value):
    """Ensures that the value is lesser than 25 but greater than -1"""
    
    # all positive cases
    if value > -1:
        while value > 85:
            #return validate(value - 26)    #recursive
            value-=85
            
    # all negative cases
    else:
        while value < 0:
            #return validate(value + 26)    #recursive
            value+=85
            
    return value


def encode(message, shift):
    """Encoder. Shifts alphabet as per shift argument"""
    encoded_message = ""
    for letter in message:
        #print(alphabet_index[letter] + shift)
        shifted_alphabet_index = validate(alphabet_index[letter] + shift)
        #print(shifted_alphabet_index)
        encoded_message += index_alphabet[shifted_alphabet_index]
    return encoded_message
    
def decode(message, shift):
    return encode(message, -shift)

#welcome message
print("""
\nWelcome to the Encoder-Decoder Program.\n
From the menu below, please chose whether you wish to encode  or
decode a message.

""")
# Do you wish to encode or decode
operation = input("Encode or Decode: Type first letter to choose :: ")
# Type your message to decode
message = input("\nGreat! Now type your message to encode/decode here :: ")
shift = int(float(input("\n By how much is the message to be shifted :: ")))
if operation == "e":
    print(f"The encoded message is : \n\n{encode(message, shift)}")
elif operation == "d":
    print(f"The decoded message is : \n\n{decode(message, shift)}")

# give result