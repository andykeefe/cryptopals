def xor_decryption(encoded_string, key):
    decrypted = ""
    for byte in encoded_string:
        decrypted += chr(byte ^ key)
	# print(decrypted) 
	""" will show all possible decrypted texts.
	You could find the plain text manually by searching through all options if you
	really wanted to. But we are not that crazy. Uncomment print(decrypted) to see. 
 	"""
    return decrypted
    
    """
	First we initialize an empty string that will contain decrypted text. The next line
	starts a loop that will iterated over each byte in the hex_encoded_string. While looping,
	we XOR each bytes of the string with a key, convert it to a character, and add it to the
	decrypted string we initialized. Finally once all bytes have been XORed the decrypted string
	is returned.
    """

    
def english_frequency(letters):
    freq = {'a': 8.12, 'b': 1.49, 'c': 2.71, 'd': 4.32, 'e': 12.02, 'f': 2.30, 'g': 2.03,
            'h': 5.92, 'i': 7.31, 'j': 0.10, 'k': 0.69, 'l': 3.98, 'm': 2.61, 'n': 6.95,
            'o': 7.68, 'p': 1.82, 'q': 0.11, 'r': 6.02, 's': 6.28, 't': 9.10, 'u': 2.88,
            'v': 1.11, 'w': 2.09, 'x': 0.17, 'y': 2.11, 'z': 0.07, ' ': 20.0}
    score = sum(freq.get(char.lower(), 0) for char in letters)
    return score


    """
	First we define the frequency of letters in an English based on some large sample of words.
	In this case, I used measurements from Cornell University which can be found here:
	
	https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
	
	This is old data but it should hold. English hasn't changed that much. Let's start inside
	the sum() function.
	
	freq.get() method represents a dictionary lookup. car.lower() converts the character to lowercase
	so that case sensitivity is not an issue. 0 represents a default in case the character is not
	found in the freq dictionary. So the whole line 
				freq.get(char.lower(), 0) for char in letters)
	represents a generator expression. It generates a frequency for every character in the input text.
	Finally the sum function adds up all frequencies generated and calculates a total score based on 
	the frequency of letters in English. 
    """

    
def xor_key(encoded_string):
    decoded_txt = []
    for key in range(256):
        operation_decrypt = xor_decryption(encoded_string, key)
        score = english_frequency(operation_decrypt)
        decoded_txt.append((operation_decrypt, score))
    return max(decoded_txt, key=lambda x: x[1])[0]


    """ 
	First we initialize an empty list decoded_txt. Then we iterate over all possible
	key values from 0 to 255 using our defined xor_decryption() function, which we'll discuss
	more above this. A score is calculated using the english_frequency function, which, again,
	we will discuss above. 
	
	Finally, it returns the result with the highest score using the max() function. This is a
	little confusing if you don't know Python very well. max() returns maximum value of a list 
	or iterable. Our variable, decoded_txt, represents the list of decrypted values with their 
	"score." The max() function uses the key to determine the maximum value. lamda x: x[1] returns
	the second element of the tuple, in this case, the score. The highest score will be the value
	that is chosen by max() function, and the [0] represents the first item in the tuple, the
	decrypted text itself.
    """

   
def main():
    hex_encoded_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    bytes_encoded_string = bytes.fromhex(hex_encoded_string)
    operation_decrypt = xor_key(bytes_encoded_string)
    print("\nMost likely plaintext:", operation_decrypt)
    
    """ 
	First we take our hex string and convert it to bytes using bytes.fromhex() function.
	We input the result bytes_encoded_string to our xor_key() function. 
    """

if __name__ == '__main__':
	main()
